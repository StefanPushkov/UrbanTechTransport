import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

DATA = 'E:/HACKS/URBAN_TECH/DATA/tr_data_2.csv'


def predict(transportId: int, routeId: str, pathId: str,lat: float, lon: float):
    path_id_dict = {'efede61e-4529-4e61-89f3-d2cdfe192bf4': 0, 'ad8fb052-2c6b-4380-9b51-16adddfb9f79': 1,
                    'e193c6f4-9cfc-4f56-b378-8141c82f28e3': 2, 'e72ca6c2-0b0f-4e22-80aa-2dbcae29af94': 3,
                    '5cce945a-11a0-4fa3-acac-45a75cf90433': 4, 'f3710f5f-c426-4623-a722-8050aed72b55': 5,
                    'ad247399-ca47-49b6-9e13-ed8f28c7b735': 6, 'a47d713b-e403-4275-bcbc-2fadb05a48a0': 7,
                    'b692dbbd-db26-4f04-bc2d-a0df3db545eb': 8, 'd0e57372-9774-4f5f-8fc1-c889be3c5be8': 9,
                    'ff9ab04f-312d-487b-9f0c-54c30e9f687f': 10, 'c7541be6-27d9-4942-be88-07f7421d508e': 11,
                    '3bd28b0a-6ecf-4388-9fa3-2ff904e00f1c': 12, 'e85fa195-d9ae-40cf-ae6d-2b775d571eae': 13,
                    '74456807-303a-47c6-a41c-84c9a4874b81': 14, '852f94ea-f586-4e9a-a3a1-fab123e09730': 15,
                    '2f246f9e-245e-4388-b23c-7fdb2200ecbb': 16, 'a2f90eae-d5fe-4a2a-931d-8fc682e40d60': 17,
                    'b7e7af5c-31ff-43e5-b707-4b3c997eb7ed': 18}
    transportId_dict = {62825: 0, 59198: 1, 128909: 2, 9982: 3, 63312: 4, 160978: 5, 58726: 6, 59014: 7, 121116: 8,
                        62811: 9, 62818: 10, 1083790: 11, 59275: 12, 63309: 13, 160711: 14, 217377: 15, 63211: 16,
                        63490: 17, 59286: 18, 60681: 19, 57787: 20, 58932: 21, 1202925: 22, 54568: 23, 172311: 24,
                        856639: 25, 61253: 26, 172468: 27, 12623: 28, 63337: 29, 168069: 30, 978905: 31, 59814: 32,
                        59356: 33, 63307: 34, 63212: 35, 63214: 36, 168488: 37, 58795: 38}
    routeId_dict = {'663d2b8a-90c0-419c-8901-77f1afa67291': 0, '526cdc1b-a75d-43e3-be64-b68560293caa': 1,
                    '8c30dfbe-f27f-4ccb-ba7b-ca39389c91fc': 2, '66accee5-56b8-4ab8-9b8c-bc03f5c26576': 3,
                    '09f23f35-6ade-47e4-be6b-0c4afeb0b1ae': 4, 'cd07fe50-0e1c-4096-a0bb-72ac7a4e3718': 5,
                    '682f4374-87e2-4a01-ba70-c3719d0395e7': 6}

    def get_key_path(val):
        for key, value in path_id_dict.items():
            if val == key:
                return value
    path_id = get_key_path(pathId)

    def get_key_transport(val):
        for key, value in transportId_dict.items():
            if val == key:
                return value
    transportId = get_key_transport(transportId)

    def get_key_route(val):
        for key, value in routeId_dict.items():
            if val == key:
                return value
    routeId = get_key_route(routeId)


    model = load('E:/HACKS/URBAN_TECH/Main/model.joblib')

    answ = model.predict([[transportId, routeId, path_id, lat, lon]])
    return answ

print(predict(58726,'526cdc1b-a75d-43e3-be64-b68560293caa','ad8fb052-2c6b-4380-9b51-16adddfb9f79',55.819317,37.638763))