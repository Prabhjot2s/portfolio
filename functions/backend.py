import pandas as pd
import requests

API_KEY = 'fe7e929baae77d6ffa5a9e34220dd05d'


def data(city, forcast_days, kind):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt={forcast_days * 8}'
    data = requests.get(url)
    data = data.json()
    temperature = []
    x_axis = []
    if kind == "Temperature":
        temperature = [data['list'][i]['main']['temp'] for i in range(len(data['list']))]
    elif kind == "Sky":
        temperature = [data['list'][i]['weather'][0]['main'] for i in range(len(data['list']))]

    x_axis = [data['list'][i]['dt_txt'] for i in range(len(data['list']))]

    data_frame = pd.DataFrame(data={"Time": x_axis, "Temperature": temperature})

    return data_frame



