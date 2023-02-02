import pandas as pd
import numpy as np
import os

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

__author__ = 'Hannah Robertson'
__date__ = '11/19/2022'

__assignment = 'MS5'


#trains the models
def trn_model(path, out):
    for i in os.scandir(path):
        if 'Contains' not in str(i):
            df_trn = pd.read_csv(path + i.name)

            iName = i.name.replace('.csv', '')

            np_trn_x = df_trn['Urb_Index'].to_numpy()
            np_trn_y = df_trn[iName].to_numpy()

            df_model = pd.DataFrame()
            df_model['Urb_Index'] = ""

            try:
                man_reg = leastSquares(formatArr(np_trn_x), np_trn_y)
                # print('Least Squares ' + iName + ' Overall: \t' + 'y = ' + str(man_reg[0]) + 'x + ' + str(man_reg[1]))
                df_model['Least_Squares'] = {'M': man_reg[0], 'B': man_reg[1]}
            except:
                print(str(i))

            sklearn_ridge = Ridge().fit(formatArr(np_trn_x), np_trn_y)
            # print('Sklearn Ridge ' + iName + ' Overall: \t' + 'y = ' + str(sklearn_ridge.coef_[0]) + 'x + ' + str(
            # sklearn_ridge.intercept_))
            df_model['SKL_Ridge'] = {'M': sklearn_ridge.coef_[0], 'B': sklearn_ridge.intercept_}

            sklearn_lasso = Lasso().fit(formatArr(np_trn_x), np_trn_y)
            # print('Sklearn Lasso ' + iName + ' Overall: \t' + 'y = ' + str(sklearn_lasso.coef_[0]) + 'x + ' + str(
            # sklearn_lasso.intercept_))
            df_model['SKL_Lasso'] = {'M': sklearn_lasso.coef_[0], 'B': sklearn_lasso.intercept_}

            df_model_Pop_Density = pd.DataFrame()
            df_model_Income = pd.DataFrame()
            for j in range(9):
                temp = df_trn[df_trn['Urb_Index'] == (j + 1)]

                if temp.size > 0:
                    x = temp['Pop_Density'].to_numpy()
                    y = temp[iName].to_numpy()

                    try:
                        man_reg = leastSquares(formatArr(x), y)
                        # print('Least Squares Pop Dens \t' + iName + ' ' + str(j + 1) + ': \t' + 'y = ' + str(
                        # man_reg[0]) + 'x + ' + str(man_reg[1]))
                        df_model_Pop_Density['Least_Squares_' + str(j + 1)] = [man_reg[0], man_reg[1]]
                    except:
                        df_model_Pop_Density['Least_Squares_' + str(j + 1)] = [0, 0]

                    sklearn_ridge = Ridge().fit(formatArr(x), y)
                    # print('Sklearn Ridge Pop Dens \t' + iName + ' ' + str(j + 1) + ': \ty = ' + str(
                    # sklearn_ridge.coef_[0]) + 'x + ' + str(sklearn_ridge.intercept_))
                    df_model_Pop_Density['SKL_Ridge_' + str(j + 1)] = [sklearn_ridge.coef_[0], sklearn_ridge.intercept_]

                    sklearn_lasso = Lasso().fit(formatArr(x), y)
                    # print('Sklearn Lasso Pop Dens \t' + iName + ' ' + str(j + 1) + ': \ty = ' + str(
                    # sklearn_lasso.coef_[0]) + 'x + ' + str(sklearn_lasso.intercept_))
                    df_model_Pop_Density['SKL_Lasso_' + str(j + 1)] = [sklearn_lasso.coef_[0], sklearn_lasso.intercept_]

                    x = temp['Income'].to_numpy()
                    y = temp[iName].to_numpy()

                    man_reg = leastSquares(formatArr(x), y)
                    # print('Least Squares Income \t' + iName + ' ' + str(j + 1) + ': \t' + 'y = ' + str(man_reg[0])
                    # + 'x + ' + str(man_reg[1]))
                    df_model_Income['Least_Squares_' + str(j + 1)] = [man_reg[0], man_reg[1]]

                    sklearn_ridge = Ridge().fit(formatArr(x), y)
                    # print('Sklearn Ridge Income \t' + iName + ' ' + str(j + 1) + ': \ty = ' + str(
                    # sklearn_ridge.coef_[0]) + 'x + ' + str(sklearn_ridge.intercept_))
                    df_model_Income['SKL_Ridge_' + str(j + 1)] = [sklearn_ridge.coef_[0], sklearn_ridge.intercept_]

                    sklearn_lasso = Lasso().fit(formatArr(x), y)
                    # print('Sklearn Lasso Income \t' + iName + ' ' + str(j + 1) + ': \ty = ' + str(
                    # sklearn_lasso.coef_[0]) + 'x + ' + str(sklearn_lasso.intercept_))
                    df_model_Income['SKL_Lasso_' + str(j + 1)] = [sklearn_lasso.coef_[0], sklearn_lasso.intercept_]

            if not os.path.exists(out + i.name.replace('.csv', '')):
                os.makedirs(out + i.name.replace('.csv', ''))

            df_model.to_csv(out + i.name.replace('.csv', '') + '/Urb_Index_model.csv')
            df_model_Pop_Density.to_csv(out + i.name.replace('.csv', '') + '/Pop_Density_model.csv')
            df_model_Income.to_csv(out + i.name.replace('.csv', '') + '/Income_model.csv')


# i needed to reformat the arrays to make this work better
def formatArr(a):
    return np.concatenate((a.reshape(a.size, 1), np.ones(a.size).reshape(a.size, 1)), axis=1)


# this is the manual model I used; I used SKLearn for the other two.
def leastSquares(a, b):
    a_t = a.transpose()
    a_dot = np.dot(a_t, a)
    ata_inv = np.linalg.inv(a_dot)
    w = np.dot(ata_inv, a_t)
    w = np.dot(w, b)
    return w
