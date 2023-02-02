import numpy as np
import pandas as pd
import os

__author__ = "Hannah Robertson"
__date__ = "11/19/2022"

__assignment = "MS5"


def split_data(input_filename, path, fraction_training):
    """
    See homework assignment
    :param fraction_training: fraction of training set to whole
    :param path: output path
    :param input_filename: Filename for input datafile.
    """

    df = pd.read_csv(input_filename, index_col=False)
    df = df.sample(frac=1)

    df.set_index('Unnamed: 0', inplace=True)
    df = df.transpose()

    for i in df.keys():
        if i != "Urb_Index" and i != "Name" and i != "Population" and i != "Area" and i != "ST_ABV" \
                and "Category" not in i:
            df_trn = df.sample(frac=fraction_training)

            trn_w = df_trn["Income"]
            trn_x = df_trn['Urb_Index']
            trn_y = df_trn[i]

            df_trn['Pop_Density'] = df_trn['Population'].astype('double') / df_trn["Area"].astype('double')
            trn_z = df_trn['Pop_Density']

            pd.set_option('use_inf_as_na', True)
            model_trn = pd.concat([trn_w, trn_x, trn_y, trn_z], join='outer', axis=1).dropna()

            path1 = path + '/trn/'
            if not os.path.exists(path1):
                os.makedirs(path1)

            model_trn.to_csv(path1 + i + ".csv")

            df_tst = df.drop(df_trn.index)

            tst_w = df_tst["Income"]
            tst_x = df_tst['Urb_Index']
            tst_y = df_tst[i]

            df_tst['Pop_Density'] = df_tst['Population'].astype('double') / df_tst["Area"].astype('double')
            tst_z = df_tst['Pop_Density']

            pd.set_option('use_inf_as_na', True)
            model_tst = pd.concat([tst_w, tst_x, tst_y, tst_z], join='outer', axis=1).dropna()

            path2 = path + '/tst/'
            if not os.path.exists(path2):
                os.makedirs(path2)

            model_tst.to_csv(path2 + i + ".csv")


def eval_predictions(path, outpath):
    dict_best = {}

    for i in os.scandir(path):
        if '.csv' in i.name:
            df_tst = pd.read_csv(path + i.name)
        else:
            continue
        vals = ["Pop_Density", "Income"]
        methods = ["Least_Squares", "SKL_Lasso", "SKL_Ridge"]
        iName = i.name.replace(".csv", "")

        if os.path.exists(outpath + "methodData/" + iName + "/data.csv"):
            df_this = pd.read_csv(outpath + "methodData/" + iName + "/data.csv")
            df_this = df_this.set_index("Unnamed: 0")

        else:
            df_this = pd.DataFrame()

        for val in vals:
            for method in methods:
                x = df_tst[val].to_numpy()
                y_real = df_tst[iName].to_numpy()
                y_predicted = df_tst[val + "_" + method].to_numpy()

                MSE = calcMSE(x, y_real, y_predicted)
                RSS = np.sum(np.square(y_predicted - y_real))

                if val + "_" + method in df_this.keys():
                    df_this.at["MSE", val + "_" + method] = df_this.at["MSE", val + "_" + method] + MSE
                    df_this.at["RSS", val + "_" + method] = df_this.at["RSS", val + "_" + method] + RSS
                    df_this.at["this_MSE", val + "_" + method] = MSE
                    df_this.at["this_RSS", val + "_" + method] = RSS
                else:
                    df_this[val + "_" + method] = {"RSS": RSS, "MSE": MSE, "this_RSS": RSS, "this_MSE": MSE}

        if not os.path.exists(outpath + "methodData/" + iName + "/"):
            os.makedirs(outpath + "methodData/" + iName + "/")

        dict_trans = df_this.transpose()

        minMSE = list(dict_trans["MSE"]).index(min(dict_trans["MSE"]))
        minRSS = list(dict_trans["RSS"]).index(min(dict_trans["RSS"]))

        if "sum" in df_this.keys():
            df_this["sum"] = int(df_this["sum"][0].copy()) + 1
        else:
            df_this["sum"] = 1

        fmeth = open(outpath + "methodData/" + iName + "/runData.txt", "a")
        fmeth.write("Run " + str(df_this["sum"][0]) + ":\n")
        fmeth.write(df_this.keys()[minMSE] + " has best MSE. \nAVG:" + str(df_this[df_this.keys()[minMSE]]["MSE"] /
                                                                           df_this["sum"][0])
                    + "\nTHIS: " + str(df_this[df_this.keys()[minMSE]]["this_MSE"]) + "\n")
        fmeth.write(df_this.keys()[minRSS] + " has best RSS. \nAVG:" + str(df_this[df_this.keys()[minRSS]]["RSS"] /
                                                                           df_this["sum"][0])
                    + "\nTHIS: " + str(df_this[df_this.keys()[minRSS]]["this_RSS"]) + "\n\n")
        fmeth.close()

        df_this.to_csv(outpath + "methodData/" + iName + "/data.csv")

        dict_best[iName] = {"name": df_this.keys()[minMSE],
                            "MSE": (df_this[df_this.keys()[minMSE]]["MSE"] / df_this["sum"][0]),
                            "RSS": (df_this[df_this.keys()[minMSE]]["RSS"] / df_this["sum"][0])}

    f2 = open(outpath + "summary.txt", "w")
    for j in dict_best.keys():
        f2.write(j + "\n\nBest Fit: " + dict_best[j]["name"] + "\navg MSE: " + str(dict_best[j]["MSE"]) + "\navg RSS: "
                 + str(dict_best[j]["RSS"]) + "\n\n")
    f2.close()


def generate_experiment(path):
    vary = ['income/', 'pop_density/', 'both/', 'inverse/']
    for var in vary:
        pathVar = path + var
        if not os.path.exists(pathVar):
            os.makedirs(pathVar)
        for scan in os.scandir("data_processed/_datasets/tst/"):
            df = pd.read_csv("data_processed/_datasets/tst/" + scan.name)
            df = df.iloc[0:0]
            for i in range(9):
                for j in range(100):
                    if var == "income/":
                        df.loc[len(df.index)] = ['EXPERIMENTAL_DATA', j * 100, i + 1, 7, 100]
                    elif var == "pop_density/":
                        df.loc[len(df.index)] = ['EXPERIMENTAL_DATA', 50000, i + 1, 7, j]
                    elif var == "both/":
                        df.loc[len(df.index)] = ['EXPERIMENTAL_DATA', j, i + 1, 7, j]
                    else:
                        df.loc[len(df.index)] = ['EXPERIMENTAL_DATA', j, i + 1, 7, 100 - j]
            df.to_csv(pathVar + scan.name)
        print("gen")


def calcMSE(x, y_real, y_predicted):
    sums = 0
    for i in range(x.size):
        sums = sums + ((y_real[i] - y_predicted[i]) * (y_real[i] - y_predicted[i]))
    return sums / x.size
