import pandas as pd
import json
import pyarrow as pa
from datetime import datetime

def resumencreditosactivos(archivo):
    data=pd.read_csv(archivo,encoding='utf-8')
    datos=pd.DataFrame(data)
    filtrado=datos.loc[:, ['tipoDeOtorgante',
                           'tipoDeCredito',
                           'moneda',
                           'original',
                           'vigente',
                           '1_29Dias',
                           '30_59Dias',
                           '60_89Dias',
                           '90_119Dias',
                           '120_179Dias',
                           'masDe180Dias',
                           'actualizadoEn']]
    agrupamiento=filtrado.groupby(['tipoDeOtorgante','tipoDeCredito'])
    cuentas_mxn = agrupamiento['moneda'].apply(lambda x: (x == 1).sum())
    cuentasEnUsd = agrupamiento['moneda'].apply(lambda x: (x == 5).sum())
    otrasMonedas = agrupamiento['moneda'].apply(lambda x: (x != 5) & (x != 1).sum())
    operaciones = filtrado.groupby(['tipoDeOtorgante', 'tipoDeCredito']).agg({ 
        'original':"sum",
        'vigente':"sum",
        '1_29Dias':"sum",
        '30_59Dias':"sum",
        '60_89Dias':"sum",
        '90_119Dias':"sum",
        '120_179Dias':"sum",
        'masDe180Dias':"sum"})
    operaciones=operaciones.assign(cuentasEnMxn=cuentas_mxn)
    operaciones=operaciones.assign(cuentasEnUsd=cuentasEnUsd)
    operaciones=operaciones.assign(otrasMonedas=otrasMonedas)
    operaciones["saldoactual"]=operaciones['vigente']+operaciones['1_29Dias']+operaciones['30_59Dias']+operaciones['60_89Dias']+operaciones['90_119Dias']+operaciones['120_179Dias']+operaciones['masDe180Dias']
    print(operaciones)
resumencreditosactivos("creditos_activos.csv")