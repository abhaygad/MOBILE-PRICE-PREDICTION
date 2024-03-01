import pandas as pd



def data_read():
    data = pd.read_csv('DATA-PHONE.csv')
    minimun_temp = data.min(axis=0)
    min_x = minimun_temp[1:7:]
    GENERAL_min, HARDWARE_min, CAMERA_min, DISPLAY_min, BATTERY_min, AUDIO_min = min_x
    values = {"COMPLETE ": GENERAL_min, "HARDWARE": HARDWARE_min, "DISPLAY": DISPLAY_min, "BATTERY": BATTERY_min,
              "AUDIO": AUDIO_min, 'CAMERA': CAMERA_min}
    data.fillna(value=values, inplace=True)
    x = data.iloc[:, [7]].values
    for i in range(263):
        for j in range(1):
            x[i][j] = x[i][j].replace(',', '')
    data['MRP'] = pd.DataFrame(x).astype(int)
    return data

def data_name():
    data = pd.read_csv('DATA-PHONE.csv')
    lables = data["NAME"]
    return lables

def data_manupulate(data, prize_limit):
    new_data = data[data['MRP'] < prize_limit]
    new_dataframe = pd.DataFrame(new_data.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]].values)

    return new_dataframe
