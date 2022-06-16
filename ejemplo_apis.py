# API DE POKEMON
def Ejemplo_api():
    source ='https://pokeapi.co/api/v2/pokemon/'
    pokemon = requests.get(
        source
    )
    data = pokemon.json()
    print(json.dumps(data,indent=4, sort_keys=True))
    
Ejemplo_api()

import pandas as pd
import json
import requests


# API DE COVID 19 USA
def ejemplo_api2():
    URL = 'https://api.covidtracking.com/v2/states/ca/2021-01-10.json'

    
    req = requests.get(URL)
    
    covid_json_meta=req.json().get("meta")
    covid_json_data=req.json().get("data")
    covid_meta_str = json.dumps(covid_json_meta)
    covid_data_str =json.dumps(covid_json_data)
    text_data= req.text
    # print(type(covid_data))
    # print(type(text_data))
    json_dict3=json.loads(covid_data_str)
    json_dict2=json.loads(covid_meta_str)
    json_dict= json.loads(text_data)
    # print(type(covid_data))
    # print(type(json_dict))

   
    # df = pd.DataFrame.from_dict(json_dict3["cases"])
    # df.to_excel("hola.xlsx")
ejemplo_api2()


# API DE LA NASA
def Api_3():
    fechas_importanes= ['2022-05-01','2022-01-07','1999-10-07']
    api_key ="JagMhCge85OgpQgSJm8iTy03FbxeuI5wmDOjj3RH"
    for fecha in fechas_importanes: 
            URL = 'https://api.nasa.gov/planetary/apod'
            info_APOD = requests.get(
                url=URL,
                params={
                    'api_key':f'{api_key}',
                    'date':f'{fecha}'
                }
            )
            json_info_APOD = info_APOD.json()
            print("\n")
            print("//////////////////")
            print(f'Titulo :{json_info_APOD["title"]} ')
            print(f'Fecha : {json_info_APOD["date"]}')
            print(f'URL : {json_info_APOD["url"]}')
            print("//////////////////")

Api_3()


# query por codigo de sucursal 
# y hacer un join 
# instalacion a sucursal 
# filtro sucursal.codigo sucursal 