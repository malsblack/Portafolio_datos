import creditosactivos
import pandas as pd
import json
import pyarrow as pa
from datetime import datetime

def resumencreditosliquidados(archivo):
    archivo2=pd.read_csv(archivo,encoding='utf-8')
    datos=pd.DataFrame(archivo2)
    filtrado=datos.loc[:, ['tipoDeOtorgante', 'tipoDeCredito','clavesDeObservacion','moneda','original','quita','dacion','pago','quebranto','contrato','tipoCambio','plazo']]
    
    conteo=filtrado.groupby(['tipoDeOtorgante','tipoDeCredito'])
    cuentas_mxn = conteo['moneda'].apply(lambda x: (x == 1).sum())
    cuentasEnUsd = conteo['moneda'].apply(lambda x: (x == 5).sum())
    otrasMonedas = conteo['moneda'].apply(lambda x: (x != 5) & (x != 1).sum())

    
    agrupamiento = filtrado.groupby(['tipoDeOtorgante', 'tipoDeCredito']).agg({
        'clavesDeObservacion': lambda x: x.str.contains('CC : Cuenta cancelada o cerrada').sum(),
        'original':'sum',
        'quita':'sum',
        'dacion':'sum',
        'pago':'sum',
        'quebranto':'sum'})

    agrupamiento=agrupamiento.assign(cuentasEnMxn=cuentas_mxn)
    agrupamiento=agrupamiento.assign(cuentasEnUsd=cuentasEnUsd)
    agrupamiento=agrupamiento.assign(otrasMonedas=otrasMonedas)
    agrupamiento = agrupamiento.rename(columns={'clavesDeObservacion': 'cuentasCerradas'})



    

    


resumencreditosliquidados("export.csv")