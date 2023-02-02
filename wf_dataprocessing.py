# Author: Hannah Robertson
import math
import os
import pandas
from zipfile import ZipFile

__author__ = "Hannah Robertson"
__date__ = "9-23-2022"
__assignment = "Project"


# do you know how many terms there are for county in the US?
# neither did I until I started this project!
# this method strips off the county, borough, parish, etc. for easier processing
def sanitize_county(county):
    county = county.lower()
    county = county.replace(" city and borough", "").replace(" city and county", "")
    county = county.replace(" parish", "").replace(" borough", "").replace(" census area", "")
    county = county.replace(" municipality", "")
    county = county.replace(" county", "")
    county = county.replace(", ", ",").replace(" ", "_")

    # Individual county discrepancies in spelling or names
    county = county.replace("lasalle", "la_salle")
    county = county.replace("skagway-hoonah-angoon", "hoonah-angoon")
    county = county.replace("wrangell-petersburg", "wrangell")

    if county.find("city") != -1 or county.find('(blank)') != -1 \
            or county.find(",") == -1 or county.split(",")[1] == "dc":
        return [False, ""]
    else:
        return [True, county]


def processor():
    dicts = {}

    # my life expectancies are a list rather than a single number
    lexFrame = pandas.read_csv('data_original/U.S._Life_Expectancy_at_Birth_by_State_and_Census_Tract_-_2010-2015.csv')

    # found a really cool document with data about various health stats by county
    # unfortunately it is too large to upload to git, so I need to upload a zip instead
    # then unzip it here.
    healthFrame = pandas.DataFrame()
    with ZipFile('data_original/PLACES__Local_Data_for_Better_Health__County_Data_2021_release.zip', 'r') as zObject:
        zObject.extractall('data_original/')
    healthFrame = pandas.read_csv('data_original/PLACES__Local_Data_for_Better_Health__County_Data_2021_release.csv')

    # auto-remove the file once it has been read, to make git updating easier.
    os.remove('data_original/PLACES__Local_Data_for_Better_Health__County_Data_2021_release.csv')
    healthFrame.drop(healthFrame[healthFrame['DataValueTypeID'] == 'CrdPrv'].index, inplace=True)
    healthFrame.fillna('(blank)', inplace=True)

    methodFrame = healthFrame["MeasureId"].drop_duplicates()

    lndFrame = pandas.read_excel('data_original/LND01.xls')
    popFrame = pandas.read_excel('data_original/POP01.xls')
    vstFrame = pandas.read_excel('data_original/VST01.xls')
    ruFrame = pandas.read_excel('data_original/NCHSURCodes2013.xlsx')
    incFrame = pandas.read_excel('data_original/Unemployment.xlsx')

    # created a for loop to merge everything into one dict
    for i in healthFrame.index:
        sanCTup = sanitize_county(str(healthFrame['LocationName'][i]) + ","
                                  + str(healthFrame['StateAbbr'][i]))
        sanC = sanCTup[1]
        if sanCTup[0]:

            if sanC not in dicts.keys():
                dicts[sanC] = {}
                dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                dicts[sanC]["Name"] = sanC

            dicts[sanC][healthFrame['MeasureId'][i]] = (healthFrame['Data_Value'][i])
            dicts[sanC][healthFrame['MeasureId'][i] + 'Category'] = (healthFrame['Category'][i])

        if i < incFrame['Area_name'].size and isinstance(incFrame['Area_name'][i], str):
            sanCTup = sanitize_county(incFrame['Area_name'][i])
            sanC = sanCTup[1]
            if sanCTup[0] and sanC.split(",")[1] != "PR" and sanC.split(",")[1] != "DC":
                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                dicts[sanC]['Income'] = incFrame["Median_Household_Income_2020"][i]

                # This document uses a different version of NSCHUR codes; my other version only goes up to 6.
                # Tweaking the two to fit; essentially codes 7-9 are various ways of saying 'podunk hamlet backwater'
                # Which is why my other doc didn't tend to use them
                if incFrame["Rural_urban_continuum_code_2013"][i] == "7" or incFrame["Rural_urban_continuum_code_2013"][
                        i] == "8" or incFrame["Rural_urban_continuum_code_2013"][i] == "9":
                    dicts[sanC]['Urb_Index'] = 6
                else:
                    dicts[sanC]['Urb_Index'] = incFrame["Rural_urban_continuum_code_2013"][i]

        if i < lexFrame['County'].size:
            sanCTup = sanitize_county(lexFrame['County'][i])
            sanC = sanCTup[1]

            if sanCTup[0] and not math.isnan(lexFrame['Life Expectancy'][i]):

                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                if 'LE_list' not in dicts[sanC].keys():
                    dicts[sanC]['LE_list'] = []

                dicts[sanC]['LE_list'].append(lexFrame['Life Expectancy'][i])

        if i < lndFrame['Areaname'].size:
            sanCTup = sanitize_county(lndFrame['Areaname'][i])
            sanC = sanCTup[1]
            if sanCTup[0]:

                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                dicts[sanC]['Area'] = lndFrame["LND010200D"][i]

        if i < popFrame['Area_name'].size:
            sanCTup = sanitize_county(popFrame['Area_name'][i])
            sanC = sanCTup[1]
            if sanCTup[0]:

                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                dicts[sanC]['Population'] = popFrame["POP010210D"][i]

        if i < vstFrame['Areaname'].size:
            sanCTup = sanitize_county(vstFrame['Areaname'][i])
            sanC = sanCTup[1]
            if sanCTup[0]:

                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                dicts[sanC]['Dth_Rate'] = vstFrame["VST210207D"][i]

        if i < ruFrame['County name'].size:
            sanCTup = sanitize_county(ruFrame['County name'][i] + "," + ruFrame['State Abr.'][i])
            sanC = sanCTup[1]
            if sanCTup[0]:

                if sanC not in dicts.keys():
                    dicts[sanC] = {}
                    dicts[sanC]["ST_ABV"] = sanC.split(",")[1]
                    dicts[sanC]["Name"] = sanC

                dicts[sanC]['Urb_Index'] = ruFrame['2013 code'][i]

    df = pandas.DataFrame.from_dict(dicts, orient='index')
    fl = pandas.read_csv("data_original/_stateList.csv")

    for i in fl['states']:
        # for whatever reason my .csvs are not writing in the right directory
        # sometimes it is very appropriate to kill a fly with a sledgehammer
        path = os.path.abspath(os.getcwd()) + "/data_processed/" + i.upper() + "/"
        if not os.path.exists(path):
            os.makedirs(path)

        # filter by state
        if i == 'usa':
            st_df = df.copy()
        else:
            st_df = df[df['ST_ABV'] == i].copy()

        # some counties had multiple life expecancies in differnet areas. here's to averaging them.
        for j in st_df["LE_list"].index:
            if not isinstance(st_df["LE_list"][j], float):
                val = sum(st_df["LE_list"][j]) / len(st_df["LE_list"][j])
                st_df.loc[j, ["LE_list"]] = val

        # create a separate file for life expectancy by urban index
        ru_df = st_df.loc[st_df['Urb_Index'] > 3].copy()
        ru_df.rename(columns={'LE_list': 'rurLE'}, inplace=True)
        ur_df = st_df.loc[st_df['Urb_Index'] <= 3].copy()
        ur_df.rename(columns={'LE_list': 'urbLE'}, inplace=True)

        dfLE = pandas.concat([ru_df['rurLE'], ur_df['urbLE']], axis=1)

        dfLE.to_csv(path + "LE.csv")

        sum_dict = {}
        rulist = ru_df['rurLE'].dropna().tolist()
        if len(rulist) > 0:
            rulist = ru_df['rurLE'].dropna().tolist()
            sum_dict['avg_rurLE'] = [sum(rulist) / len(rulist)]
        else:
            sum_dict['avg_rurLE'] = 0

        urlist = ur_df['urbLE'].dropna().tolist()
        if len(urlist) > 0:
            sum_dict['avg_urbLE'] = [sum(urlist) / len(urlist)]
        else:
            sum_dict['avg_urbLE'] = 0

        for j in methodFrame:
            #  add in urban index
            ru_df = st_df.loc[st_df['Urb_Index'] > 3].copy()
            ru_df.rename(columns={j: 'rur' + j}, inplace=True)
            ur_df = st_df.loc[st_df['Urb_Index'] <= 3].copy()
            ur_df.rename(columns={j: 'urb' + j}, inplace=True)

            if ru_df['rur' + j].dropna().size > 0:
                rulist = ru_df['rur' + j].dropna().tolist()
                sum_dict['avg_rur' + j] = sum(rulist) / len(rulist)
            if ur_df['urb' + j].dropna().size > 0:
                urlist = ur_df['urb' + j].dropna().tolist()
                sum_dict['avg_urb' + j] = sum(urlist) / len(urlist)

            sum_dict[j + "Category"] = st_df[j + "Category"][0]

        sum_df = pandas.DataFrame(sum_dict)
        sum_df.to_csv(path + "sum_data.csv")

        # transpose for easier parsing
        st_df = st_df.transpose()

        st_df.to_csv(path + "_allData.csv")


# for testing purposes, I got tired of switching back to the main
if __name__ == '__main__':
    processor()
