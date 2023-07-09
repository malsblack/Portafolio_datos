import pandas as pd
import json
import pyarrow as pa
from datetime import datetime


def Declarativa(input_data,Persona):
    if Persona=="PM" or Persona=="PFAE":
        data_consult=input_data["response"]["respuesta"]["declarativa"]
        data_consult.pop("rfc")
        data_consult.pop("fechaDeclarativa")
        name=[]
        desciption=[]
        for i in data_consult:
            name.append(i)
            desciption.append(data_consult[f"{i}"])

        
        data_export={"Declarativa":name,
                    "Descripcion":desciption} 

        data_fina=pd.DataFrame(data_export)
        print(data_fina)
        rfc=input_data["response"]["respuesta"]["datosGenerales"]["rfcCliente"]
        date=input_data["response"]["respuesta"]["encabezado"]["fechaConsulta"]
        date_consult = datetime.strptime(f"{date}", "%d%m%Y").strftime("%Y%m%d")
        data_fina.to_parquet(f'muffin_declarativa_{rfc}_{date_consult}.parquet',engine="pyarrow")     
        
    else:
        return "Persona invalida"
Declarativa(json.load(open("respuesta.json","r")),"PM")