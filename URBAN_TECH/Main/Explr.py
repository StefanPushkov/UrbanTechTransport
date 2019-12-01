import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from joblib import load, dump
from sklearn.preprocessing import StandardScaler
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


DATA = 'E:/HACKS/URBAN_TECH/DATA/tr_data_2.csv'
def ExploreData():

    # Read Data using chosen columns
    data = pd.read_csv(DATA, names=['transportId', 'routeId', 'pathId', 'lat', 'lon', 'speed', 'createdAt'])
    #data = data[data.transportId == 62825]

    '''
    # Change time format from Unix to normal
    data['createdAt'] = data['createdAt'].apply(lambda x: datetime.utcfromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'))

    #data = data[data.createdAt == ]
    data['createdAt'] = data['createdAt'].apply(lambda x: int(x[-9:].replace(':', '')))
    '''
    data = data.drop(['createdAt'], axis=1)

    list_of_pathId = list(data.pathId.unique())
    pathId_dict = {k:v for k, v in zip(list_of_pathId, list(range(len(list_of_pathId))))}
    print("path_id: ", pathId_dict)
    def get_key_route(val):
        for key, value in pathId_dict.items():
            if val == key:
                return value

    data.pathId = data.pathId.apply(lambda x: get_key_route(x))


    list_of_transportId= list(data.transportId.unique())
    transportId_dict = {k: v for k, v in zip(list_of_transportId, list(range(len(list_of_transportId))))}
    print("transportId_dict: ", transportId_dict)

    def get_key_tr(val):
        for key, value in transportId_dict.items():
            if val == key:
                return value

    data.transportId = data.transportId.apply(lambda x: get_key_tr(x))



    list_of_routeId = list(data.routeId.unique())
    routeId_dict = {k: v for k, v in zip(list_of_routeId, list(range(len(list_of_routeId))))}

    print("routeId_dict: ", routeId_dict)
    def get_key_path(val):
        for key, value in routeId_dict.items():
            # print(value)
            if val == key:

                return value

    data.routeId = data.routeId.apply(lambda x: get_key_path(x))
    print(data.routeId.iloc[:10])
    print(data[['pathId', 'transportId', 'routeId']].head())




    # data = pd.get_dummies(data, columns=['routeId', 'pathId'])

    X = data.drop(['speed'], axis=1)
    y = data[['speed']].values.ravel()

    model = RandomForestRegressor()
    model.fit(X, y)

    # Save model
    dump(model, 'E:/HACKS/URBAN_TECH/Main/model.joblib')

    '''
    chart = sns.lmplot(x='createdAt', y='speed', data=data, order=3, ci=None)
    [plt.setp(ax.get_xticklabels(), rotation=45) for ax in chart.axes.flat]
    plt.ylim(0, max(data.speed))
    plt.show()
    # Group data by routeID
    # groups = data.groupby(['routeId'])
    # for key, item in groups:
    #     print(key)
    '''


ExploreData()