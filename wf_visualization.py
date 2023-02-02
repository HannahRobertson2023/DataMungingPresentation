# Author: Hannah Robertson
import os
import pandas
from matplotlib import pyplot as plt

refDict = {
        'TEETHLOST': "All teeth lost among adults aged >=65 years",
        'ARTHRITIS': "Arthritis among adults aged >=18 years",
        'CANCER': "Cancer (excluding skin cancer) among adults aged >=18 years",
        'KIDNEY': "Chronic kidney disease among adults aged >=18 years",
        'COPD': "Chronic obstructive pulmonary disease among adults aged >=18 years",
        'CHD': "Coronary heart disease among adults aged >=18 years",
        'CASTHMA': "Current asthma among adults aged >=18 years",
        'DEPRESSION': "Depression among adults aged >=18 years",
        'DIABETES': "Diagnosed diabetes among adults aged >=18 years",
        'BPHIGH': "High blood pressure among adults aged >=18 years",
        'HIGHCHOL': "High cholesterol among adults aged >=18 years who have been screened in the past 5 years",
        'OBESITY': "Obesity among adults aged >=18 years",
        'STROKE': "Stroke among adults aged >=18 years",
        'BINGE': "Binge drinking among adults aged >=18 years",
        'CSMOKING': "Current smoking among adults aged >=18 years",
        'LPA': "No leisure-time physical activity among adults aged >=18 years",
        'SLEEP': "Sleeping less than 7 hours among adults aged >=18 years",
        'GHLTH': "Fair or poor self-rated health status among adults aged >=18 years",
        'MHLTH': "Mental health not good for >=14 days among adults aged >=18 years",
        'PHLTH': "Physical health not good for >=14 days among adults aged >=18 years",
        'CERVICAL': "Cervical cancer screening among adult women aged 21-65 years",
        'CHOLSCREEN': "Cholesterol screening among adults aged >=18 years",
        'ACCESS2': "Current lack of health insurance among adults aged 18-64 years",
        'COLON_SCREEN': "Fecal occult blood test, sigmoidoscopy, or colonoscopy among adults aged 50-75 years",
        'MAMMOUSE': "Mammography use among women aged 50-74 years",
        'COREM': "Older adult men aged >=65 years who are up to date on a core set of clinical preventive services: "
                 "Flu shot past year, PPV shot ever, Colorectal cancer screening",
        'COREW': "Older adult women aged >=65 years who are up to date on a core set of clinical preventive services: "
                 "Flu shot past year, PPV shot ever, Colorectal cancer screening, and Mammogram past 2 years",
        'BPMED': "Taking medicine for high blood pressure control "
                  "among adults aged >=18 years with high blood pressure",
        'DENTAL': "Visits to dentist or dental clinic among adults aged >=18 years",
        'CHECKUP': "Visits to doctor for routine checkup within the past year among adults aged >=18 years"
    }


def create_visualization():
    # I know this is visualization but this allows me a cool way of slaving my for loop to an external source
    fl = pandas.read_csv("data_original/_stateList.csv")

    # allows me to make a different file for each state
    for i in fl['states']:
        # life expectancy is tricky; it requires its own style of graph
        df = pandas.read_csv("data_processed/" + i.upper() + "/LE.csv")

        urbLE = []
        rurLE = []

        if 'urbLE' in df:
            urbLE = df["urbLE"].dropna()
        if 'rurLE' in df:
            rurLE = df["rurLE"].dropna()

        fig, axs = plt.subplots(1, 2)

        if len(urbLE) > 0:
            axs[0].set(title='Average Urban Life Expectancy',
                       ylabel='Amount', xlabel='Life Expectancy')
            axs[0].hist(urbLE, bins=10, density=True)
        else:
            axs[0].set(title='No Urban Data')

        if len(rurLE) > 0:
            axs[1].set(title='Average Rural Life Expectancy',
                       ylabel='Amount', xlabel='Life Expectancy')
            axs[1].hist(rurLE, bins=10, density=True)
        else:
            axs[1].set(title='No Rural Data')

        path = "visuals/" + i.upper()
        if not os.path.exists(path):
            os.makedirs(path)
        plt.savefig(path + '/Life_Expectancy.png')
        plt.close(fig)

        # these are the graphs for the other factors of data
        df = pandas.read_csv("data_processed/" + i.upper() + "/sum_data.csv")
        for j in refDict:
            urbNum = None
            rurNum = None
            try:
                urbNum = df["avg_urb" + j][0]
            except:
                print(i + ": avg_urb" + j + " NO DATA")
                urbNum = 0
            try:
                rurNum = df["avg_rur" + j][0]
            except:
                print(i + ": avg_rur" + j + " NO DATA")
                urbNum = 0

            if urbNum > 0:
                fig, axs = plt.subplots(2, 1)
                axs[0].set(title="Urban " + refDict[j])
                axs[0].pie([urbNum, 100 - urbNum],
                           explode=[0, 0], labels=['Yes', 'No'],
                           autopct="%.f", startangle=90)
                axs[0].axis('equal')
            else:
                axs[0].set(title='No Urban Data')

            if len(rurLE) > 0:
                axs[1].set(title="Rural " + refDict[j])
                axs[1].pie([rurNum, 100 - rurNum],
                           explode=[0, 0], labels=['Yes', 'No'],
                           autopct="%.f", startangle=90)
                axs[1].axis('equal')
            else:
                axs[1].set(title='No Rural Data')

            pathJ = ""
            try:
                pathJ = path + "/" + df[j + "Category"][0].replace(" ", "_") + "/"
                if not os.path.exists(pathJ):
                    os.makedirs(pathJ)
                plt.savefig(pathJ + j + '.png')
            except:
                print(j + "Category: " + str(df[j + "Category"][0]))

            plt.close()


# for testing purposes, I got tired of switching back to the main
if __name__ == '__main__':
    create_visualization()