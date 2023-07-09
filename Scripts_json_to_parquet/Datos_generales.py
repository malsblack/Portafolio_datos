import pandas as pd
import json
import pyarrow as pa
from datetime import datetime

def Datos_generales(input_data,Persona):
    if Persona=="PM" or Persona=="PFAE":
        cliente={'1':'PM','2':'PFAE','3':'Fondo o Fideicomiso','4':'Fondo o Fideicomiso'}
        data_consult={"rfcCliente":"",
                    "nombre":"",
                    "tipoCliente":"",
                    "pais":"",
                    "actividadEconomica1":"",
                    "actividadEconomica2":"",
                    "actividadEconomica3":""}

        for tabla in data_consult:
            if tabla in input_data["response"]["respuesta"]["datosGenerales"]:
                if input_data["response"]["respuesta"]["datosGenerales"][f"{tabla}"]!=None:
                    data_consult[f"{tabla}"]=input_data["response"]["respuesta"]["datosGenerales"][f"{tabla}"]
                else:
                    pass
            else:
                pass
        
        data_export={"rfc":data_consult["rfcCliente"],
                    "nombre":data_consult["nombre"],
                    "persona":cliente[data_consult["tipoCliente"]],
                    "nacionalidad":data_consult["pais"],
                    "actividadEconomica":data_consult["actividadEconomica1"]+data_consult["actividadEconomica2"]+data_consult["actividadEconomica3"]}

        data_fina=pd.DataFrame(data_export,index=[0])
        print(data_fina)
        date=input_data["response"]["respuesta"]["encabezado"]["fechaConsulta"]
        date_consult = datetime.strptime(f"{date}", "%d%m%Y").strftime("%Y%m%d")
        data_fina.to_parquet(f'moffin_datosGenerales_{data_export["rfc"]}_{date_consult}.parquet',engine="pyarrow")
    elif Persona=="PF":
        data_consult={"ApellidoPaterno":"",
                    "ApellidoMaterno":"",
                    "PrimerNombre":"",
                    "SegundoNombre":"",
                    "FechaNacimiento":"",
                    "RFC":"",
                    "NumeroRegistroElectoral":"",
                    "ClaveImpuestosOtroPais":""}  
        for tabla in data_consult:
            if tabla in input_data["response"]["return"]["Personas"]["Persona"]["Nombre"]:
                if input_data["response"]["return"]["Personas"]["Persona"]["Nombre"][f"{tabla}"]!=None:
                    data_consult[f"{tabla}"]=input_data["response"]["return"]["Personas"]["Persona"]["Nombre"][f"{tabla}"]
                else:
                    pass
            else:
                pass
        data_export={"nombre":data_consult["PrimerNombre"]+" "+data_consult["SegundoNombre"],
                     "apellidos":data_consult["ApellidoPaterno"]+" "+data_consult["ApellidoMaterno"],
                     "rfc":data_consult["RFC"],
                     "fechaNacimiento":datetime.strptime(f"{data_consult['FechaNacimiento']}", "%d%m%Y").strftime("%Y-%m-%d"),     
                     "ine":data_consult["NumeroRegistroElectoral"],
                     "curp":data_consult["ClaveImpuestosOtroPais"],
                     "registroEnBc":datetime.strptime(f"{input_data['updatedAt']}", "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")}
        
        date_consult = datetime.strptime(f"{input_data['response']['respuesta']['encabezado']['fechaConsulta']}", "%d%m%Y").strftime("%Y%m%d")
        data_fina=pd.DataFrame(data_export,index=[0])
        print(data_fina)
        data_fina.to_parquet(f'moffin_datosGenerales_{data_export["rfc"]}_{date_consult}.parquet',engine="pyarrow")
   
        

Datos_generales(json.load(open("respuesta.json","r")),"PM")