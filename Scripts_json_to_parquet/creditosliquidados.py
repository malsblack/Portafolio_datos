import pandas as pd
import json
import pyarrow as pa
from datetime import datetime

def CreditosLiquidados(input_data,Persona):
    if Persona=="PM" or Persona=="PFAE":
        dic_credito={"1300":"ARREN PURO",
                "1301":"DESCUENTOS",
                "1302":"QUIROG",
                "1303":"COLATERAL",
                "1304":"PRENDAR",
                "1305":"SIMPLE",
                "1306":"P.G.U.I.",
                "1307":"HABILITACION",
                "1308":"REFACC",
                "1309":"I.E.P.B.S.",
                "1310":"VIVIENDA",
                "1311":"O.C. GARANTIA INMOB",
                "1314":"NO DISPONIBLE",
                "1316":"O.A.V.",
                "1317":"C.V.A.",
                "1320":"ARREN VIGENTE",
                "1321":"ARREN SINDICADO",
                "1322":"ARREND",
                "1323":"REESTRUCTURADOS",
                "1324":"RENOVADOS",
                "1327":"ARR. FINAN. SINDICADO",
                "1340":"REDESCUENTO",
                "1341":"O. REDESCUENTO",
                "1342":"RED. REESTRUCTURADOS",
                "1350":"PRESTAMOS C/FIDEICOMISOS GARANTÍA",
                "1380":"T. CRED. EMPRESARIALCORPORATIVA",
                "2303":"CARTAS DE CREDITO",
                "3011":"FACTORAJE C/REC",
                "3012":"FACTORAJE S/REC",
                "3230":"ANT.A.C.P.P.FACTORAJE",
                "3231":"ARREN VIGENTE",
                "6103":"ADEUDOS POR AVAL",
                "6105":"CARTAS DE CRÉDITOS NO DISPUESTAS",
                "6228":"FIDEICOMISOS PLANTA PRODUCTIVA",
                "6229":"UDIS FIDEICOMISOS EDOS",
                "6230":"UDIS FIDEICOMISOS VIVIENDA",
                "6240":"ABA PASEM II",
                "6250":"TARJETA DE SERVICIO",
                "6260":"CRÉDITO FISCAL",
                "6270":"CRÉDITO AUTOMOTRIZ",
                "6280":"LÍNEA DE CRÉDITO",
                "6290":"SEGUROS",
                "6291":"FIANZAS",
                "6292":"FONDOS Y FIDEICOMISOS"}
        
        clave_observacion={
            "AD":"Cuenta o monto en aclaración directamente con el Usuario",
            "CA":"Cuenta al corriente vendida o cedida a un Usuario de una Sociedad de Información Crediticia.",
            "CC":"Cuenta cancelada o cerrada",
            "CL":"Cuenta en cobranza pagada totalmente, sin causar quebranto",
            "CO":"Crédito en controversia",
            "CP":"Crédito hipotecario con bien inmueble declarado cómo pérdida parcial o total a causa de catástrofe natural, liquidado parcialmente por pago de Aseguradora",
            "CT":"Crédito hipotecario con bien inmueble declarado cómo pérdida parcial o total a causa de catástrofe natural, liquidado parcialmente por pago de Aseguradora",
            "CV":"Cuenta que no está al corriente vendida o cedida a un Usuario de Buró de Crédito",
            "FD":"Cuenta con fraude atribuible al Cliente",
            "FN":"Fraude NO atribuible al Cliente",
            "FP":"Fianza pagada",
            "FR":"Adjudicación y/o aplicación de garantía",
            "GP":"Ejecución de Garantía Prendaria o Fiduciaria en Pago por Crédito.",
            "IA":"Cuenta Inactiva",
            "IM":"Integrante Causante de Mora",
            "IS":"Integrante que fue subsidiado para evitar mora.",
            "LC":"Convenio de finiquito con pago menor a la deuda, acordado con el Cliente (Quita)",
            "LG":"Pago menor de la deuda por programa institucional o de gobierno, incluyendo los apoyos a damnificados por catástrofes naturales (Quita)",
            "LO":"En Localización",
            "LS":"Tarjeta de Crédito robada o extraviada",
            "NA":"Cuenta al corriente vendida o cedida a un No Usuario de Buró de Crédito.",
            "NV":"Cuenta vencida vendida a un No Usuario de una Sociedad de Información Crediticia.",
            "PC":"Cuenta en Cobranza",
            "RA":"Cuenta reestructurada sin pago menor, por programa institucional o gubernamental, incluyendo los apoyos a damnificados por catástrofes naturales",
            "RI":"Robo de identidad",
            "RF":"Resolución judicial favorable al Cliente",
            "RN":"Cuenta reestructurada debido a un proceso judicial",
            "RV":"Cuenta reestructurada sin pago menor por modificación de la situación del cliente, a petición de éste.",
            "SG":"Demanda por el Usuario",
            "UP":"Cuenta que causa castigo y/o quebranto",
            "VR":"Dación en pago o Renta"
        }
        
        data_consult={"numeroCuenta":"",
                    "tipoUsuario":"",
                    "tipoCredito":"",
                    "moneda":"",
                    "tipoCambio":"",
                    "apertura":"",
                    "plazo":"",
                    "saldoInicial":"",
                    "atrasoMayor":"",
                    "historicoPagos":"",
                    "claveObservacion":"",
                    "fechaCierre":"",
                    "quita":"",
                    "dacion":"",
                    "pagoCierre":"",
                    "quebranto":"",
                    "ultimoPeriodoActualizado":""}
        data_export=[]
        
        for i in range(len(input_data["response"]["respuesta"]["creditoFinanciero"])):
            for clave in data_consult:
                data_consult[clave] = ""
            for tabla in data_consult:
                if tabla in input_data["response"]["respuesta"]["creditoFinanciero"][i]:
                    if input_data["response"]["respuesta"]["creditoFinanciero"][i][f"{tabla}"]!=None:
                        data_consult[f"{tabla}"]=input_data["response"]["respuesta"]["creditoFinanciero"][i][f"{tabla}"]
                    else:
                        data_consult[f"{tabla}"]=""
                        pass
                else:
                    pass
            x=0
            data_translate={
                "contrato":data_consult["numeroCuenta"],
                "tipoDeOtorgante":data_consult["tipoUsuario"],
                "tipoDeCredito":dic_credito[data_consult["tipoCredito"]],
                "moneda":data_consult["moneda"],
                "tipoCambio":data_consult["tipoCambio"],
                "otorgadoEn":datetime.strptime(f"{data_consult['apertura']}", "%d%m%Y").strftime("%Y-%m-%d"),
                "plazo":int(data_consult["plazo"]) if data_consult["plazo"] and data_consult["plazo"].strip() else 0,
                "original":int(data_consult["saldoInicial"]) if data_consult["saldoInicial"] and data_consult["saldoInicial"].strip() else 0,
                "diasDeAtraso":int(data_consult["atrasoMayor"]) if data_consult["atrasoMayor"] and data_consult["atrasoMayor"].strip() else 0,
                "historicoDePagos":int(data_consult["historicoPagos"]) if data_consult["historicoPagos"] and data_consult["historicoPagos"].strip() else 0,
                "clavesDeObservacion":f"{data_consult['claveObservacion']} : {clave_observacion[data_consult['claveObservacion']]}" if data_consult["claveObservacion"] and data_consult["claveObservacion"].strip() else "",
                "liquidadoEn":int(data_consult["fechaCierre"]) if data_consult["fechaCierre"] and data_consult["fechaCierre"].strip() else 0,
                "quita":int(data_consult["quita"]) if data_consult["quita"] and data_consult["quita"].strip() else 0,
                "dacion":int(data_consult["dacion"]) if data_consult["dacion"] and data_consult["dacion"].strip() else 0,
                "pago":int(data_consult["pagoCierre"]) if data_consult["pagoCierre"] and data_consult["pagoCierre"].strip() else 0,
                "quebranto":int(data_consult["quebranto"]) if data_consult["quebranto"] and data_consult["quebranto"].strip() else 0,
                "actualizadoEn":datetime.strptime(f"{data_consult['ultimoPeriodoActualizado']}", "%Y%m").strftime("%Y-%m-%d")
            }
            data_export.append(data_translate)

        
        export=pd.DataFrame(data_export)
        rfc=input_data["response"]["respuesta"]["creditoFinanciero"][0]["rfcCliente"]
        print(rfc)
        export.to_parquet(f'g.parquet',engine="pyarrow",int96_timestamp_unit='ms')
        print(export)
        
        
  
   
        

CreditosLiquidados(json.load(open("respuesta.json","r")),"PM")