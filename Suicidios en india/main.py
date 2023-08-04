import requests
import json
import pandas as pd
import sys
  
def extraccion(data_url):
    try:
        response=requests.get(data_url)
        if response.status_code==200:
            data=response.json()
            return data
        
    except requests.exceptions.RequestException as e:
        print('Error en la solicitud:', e)

def transformacion(data):
    df_origen=pd.DataFrame(data)
    df_nuevo=pd.DataFrame()
    print(df_origen.describe)
    df_nuevo["Comun","Official","native"]=df_origen["name"].str.split(",",1,expand=True)
    print(df_nuevo)
        

        
    
    
transformacion(extraccion("https://restcountries.com/v3.1/all"))
