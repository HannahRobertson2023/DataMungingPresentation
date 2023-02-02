import pandas as pd
import os

__author__ = "Hannah Robertson"
__date__ = "11/19/2022"

__assignment = "MS5"


def test_model(path, out):
    for i in os.scandir(path):
        df_tst = pd.read_csv(path + i.name)

        models = ['Urb_Index', 'Pop_Density', 'Income']
        methods = ["Least_Squares", "SKL_Lasso", "SKL_Ridge"]

        dict_pred = {}

        for index, row in df_tst.iterrows():
            for model in models:
                df_model = pd.read_csv("models/" + i.name.replace('.csv', '') + '/' + model + '_model.csv')
                for method in methods:
                    if model != "Urb_Index":
                        tag = method + "_" + str(int(row["Urb_Index"]))
                    else:
                        tag = method

                    m = df_model[tag][0].astype(float)
                    b = df_model[tag][1].astype(float)

                    out_tag = model + "_" + method
                    if out_tag not in dict_pred.keys():
                        dict_pred[out_tag] = []
                        dict_pred[out_tag + "_m"] = []
                        dict_pred[out_tag + "_b"] = []

                    dict_pred[out_tag].append(row[model] * m + b)
                    dict_pred[out_tag + "_m"].append(m)
                    dict_pred[out_tag + "_b"].append(b)

        for key in dict_pred.keys():
            df_tst[key] = dict_pred[key]

        if not os.path.exists(out):
            os.makedirs(out)

        df_tst.to_csv(out + i.name)
