import json
import pandas as pd

def transform_creditos_activos():
    TIPO_CREDITO = {"1300": "ARREN PURO",
        "1301": "DESCUENTOS",
        "1302": "QUIROG",
        "1303": "COLATERAL",
        "1304": "PRENDAR",
        "1305": "SIMPLE",
        "1306": "P.G.U.I.",
        "1307": "HABILITACION",
        "1308": "REFACC",
        "1309": "I.E.P.B.S.",
        "1310": "VIVIENDA",
        "1311": "O.C. GARANTIA INMOB",
        "1314": "NO DISPONIBLE",
        "1316": "O.A.V.",
        "1317": "C.V.A.",
        "1320": "ARREN VIGENTE",
        "1321": "ARREN SINDICADO",
        "1322": "ARREND",
        "1323": "REESTRUCTURADOS",
        "1324": "RENOVADOS",
        "1327": "ARR. FINAN. SINDICADO",
        "1340": "REDESCUENTO",
        "1341": "O. REDESCUENTO",
        "1342": "RED. REESTRUCTURADOS",
        "1350": "PRESTAMOS C/FIDEICOMISOS GARANTÍA",
        "1380": "T. CRED. EMPRESARIALCORPORATIVA",
        "2303": "CARTAS DE CREDITO",
        "3011": "FACTORAJE C/REC",
        "3012": "FACTORAJE S/REC",
        "3230": "ANT.A.C.P.P.FACTORAJE",
        "3231": "ARREN VIGENTE",
        "6103": "ADEUDOS POR AVAL",
        "6105": "CARTAS DE CRÉDITOS NO DISPUESTAS",
        "6228": "FIDEICOMISOS PLANTA PRODUCTIVA",
        "6229": "UDIS FIDEICOMISOS EDOS",
        "6230": "UDIS FIDEICOMISOS VIVIENDA",
        "6240": "ABA PASEM II",
        "6250": "TARJETA DE SERVICIO",
        "6260": "CRÉDITO FISCAL",
        "6270": "CRÉDITO AUTOMOTRIZ",
        "6280": "LÍNEA DE CRÉDITO",
        "6290": "SEGUROS",
        "6291": "FIANZAS",
        "6292": "FONDOS Y FIDEICOMISOS"}
    CLAVES_DE_OBSERVACION = {
        "AD": "{\"AD\":\"Cuenta o monto en aclaración directamente con el Usuario\"}",
        "CA": "{\"CA\":\"Cuenta al corriente vendida o cedida a un Usuario de una Sociedad de Información Crediticia.\"}",
        "CC": "{\"CC\":\"Cuenta cancelada o cerrada\"}",
        "CL": "{\"CL\":\"Cuenta en cobranza pagada totalmente, sin causar quebranto\"}",
        "CO": "{\"CO\":\"Crédito en controversia\"}",
        "CP": "{\"CP\":\"Crédito hipotecario con bien inmueble declarado cómo pérdida parcial o total a causa de catástrofe natural, liquidado parcialmente por pago de Aseguradora\"}",
        "CT": "{\"CT\":\"Crédito hipotecario con bien inmueble declarado cómo pérdida parcial o total a causa de catástrofe natural, liquidado parcialmente por pago de Aseguradora\"}",
        "CV": "{\"CV\":\"Cuenta que no está al corriente vendida o cedida a un Usuario de Buró de Crédito\"}",
        "FD": "{\"FD\":\"Cuenta con fraude atribuible al Cliente\"",
        "FN": "{\"FN\":\"Fraude NO atribuible al Cliente\"}",
        "FP": "{\"FP\":\"Fianza pagada\"}",
        "FR": "{\"FR\":\"Adjudicación y/o aplicación de garantía\"}",
        "GP": "{\"GP\":\"Ejecución de Garantía Prendaria o Fiduciaria en Pago por Crédito.\"}",
        "IA": "{\"IA\":\"Cuenta Inactiva\"}",
        "IM": "{\"IM\":\"Integrante Causante de Mora\"}",
        "IS": "{\"IS\":\"Integrante que fue subsidiado para evitar mora.\"}",
        "LC": "{\"LC\":\"Convenio de finiquito con pago menor a la deuda, acordado con el Cliente (Quita)\"}",
        "LG": "{\"LG\":\"Pago menor de la deuda por programa institucional o de gobierno, incluyendo los apoyos a damnificados por catástrofes naturales (Quita)\"}",
        "LO": "{\"LO\":\"En Localización\"}",
        "LS": "{\"LS\":\"Tarjeta de Crédito robada o extraviada\"}",
        "NA": "{\"NA\":\"Cuenta al corriente vendida o cedida a un No Usuario de Buró de Crédito.\"}",
        "NV": "{\"NV\":\"Cuenta vencida vendida a un No Usuario de una Sociedad de Información Crediticia.\"}",
        "PC": "{\"PC\":\"Cuenta en Cobranza",
        "RA": "{\"RA\":\"Cuenta reestructurada sin pago menor, por programa institucional o gubernamental, incluyendo los apoyos a damnificados por catástrofes naturales\"}",
        "RI": "{\"RI\":\"Robo de identidad\"}",
        "RF": "{\"RF\":\"Resolución judicial favorable al Cliente\"}",
        "RN": "{\"RN\":\"Cuenta reestructurada debido a un proceso judicial\"}",
        "RV": "{\"RV\":\"Cuenta reestructurada sin pago menor por modificación de la situación del cliente, a petición de éste.\"}",
        "SG": "{\"SG\":\"Demanda por el Usuario\"}",
        "UP": "{\"UP\":\"Cuenta que causa castigo y/o quebranto\"}",
        "VR": "{\"VR\":\"Dación en pago o Renta\"}"
    }
    with open("respuesta.json","r") as j:
        data=json.load(j)
        response_data = data["response"]["respuesta"]["creditoFinanciero"]
        df_credito_financiero = pd.json_normalize(response_data).reset_index(drop=True)
        df_credito_financiero_rename = df_credito_financiero.rename(
               {
                    'numeroCuenta': 'contrato', 'tipoUsuario': 'tipoDeOtorgante', 'tipoCredito': 'tipoDeCredito',
                    'moneda': 'moneda', 'tipoCambio': 'tipoCambio', 'apertura': 'otorgadoEn', 'plazo': 'plazo',
                    'saldoInicial': 'original', 'saldoVigente': 'vigente', 'saldoVencidoDe1a29Dias': '1_29Dias',
                    'saldoVencidoDe30a59Dias': '30_59Dias', 'saldoVencidoDe60a89Dias': '60_89Dias',
                    'saldoVencidoDe90a119Dias': '90_119Dias', 'saldoVencidoDe120a179Dias': '120_179Dias',
                    'saldoVencidoDe180DiasOMas': 'masDe180Dias', 'atrasoMayor': 'diasDeAtraso',
                    'historicoPago': 'historicoDePagos', 'claveObservacion': 'clavesDeObservacion',
                    'ultimoPeriodoActualizado': 'actualizadoEn'
                }, axis=1)
        df_credito_financiero_rename['tipoDeCredito'] = df_credito_financiero_rename['tipoDeCredito'].\
            map(TIPO_CREDITO)
        df_credito_financiero_rename['clavesDeObservacion'] = df_credito_financiero_rename['clavesDeObservacion'].\
            map(CLAVES_DE_OBSERVACION)
        df_credito_financiero_rename['otorgadoEn'] = pd.to_datetime(df_credito_financiero_rename['otorgadoEn'],
                                                                        format='%d%m%Y').dt.strftime('%Y-%m-%d')
        return(df_credito_financiero_rename.to_csv("creditos_activos.csv"))