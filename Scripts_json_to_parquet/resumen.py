import pandas as pd
import json
import pyarrow as pa
from datetime import datetime

def Datos_generales(input_data,Persona):
    
    if Persona=="PM" or Persona=="PFAE":
        data_consult={"calificacionCartera":"",
                    "indicadorInformacionAdicional":"",
                    "prevenciones":"",
                    "prevencionesPersona":"",
                    "prevencionesImpug":"",
                    "prevencionesPersonaImpug":""}

        for tabla in data_consult:
            if tabla in input_data:
                data_consult[f"{tabla}"]=input_data["response"]["respuesta"]["datosGenerales"][f"{tabla}"]
            else: 
                pass
        data_fina=pd.DataFrame(data_consult,index=[0])
        print(data_fina)
        rfc=input_data["response"]["respuesta"]["datosGenerales"]["rfcCliente"]
        date=input_data["response"]["respuesta"]["encabezado"]["fechaConsulta"]
        date_consult = datetime.strptime(f"{date}", "%d%m%Y").strftime("%Y%m%d")
        data_fina.to_parquet(f'muffin_resumen_{rfc}_{date_consult}.parquet',engine="pyarrow")     

    else:
        return print("Tipo de persona invalido")
Datos_generales(json.load(open("respuesta.json","r")),"P")