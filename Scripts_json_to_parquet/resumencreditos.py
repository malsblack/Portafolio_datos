import pandas as pd
import json
import pyarrow as pa

def resumen_creditos(parquet,persona):
    if persona =="PF": #No se si dejar la validacion, preguntar debido a que creditos tambien solo es para PF
        parquet=pd.read_excel(parquet) 
        datos=pd.DataFrame(parquet)
        filtrado=datos.loc[:, ['formaDePago','cierre','limiteDeCredito','creditoMaximo','saldoActual','saldoVencido','montoApagar','saldoMorosidadHistMasGrave','updatedAt']]
        filtrado['cuentas']=filtrado['formaDePago'].apply(lambda x: list(json.loads(x).keys())[0] if x!="None" else "None" ) #se obtiene la key del diccionario json, osea el 00
        filtrado=filtrado.drop("formaDePago",axis=1) #ya no me sirve la columnda
        print(filtrado)
        filtrado['cuentasCerradas']=filtrado['cierre'].apply(lambda x: 1 if x!="None" else 0) #contamos las cuentas cerradas
        filtrado['cuentasAbiertas']=filtrado['cuentasCerradas'].apply(lambda x: 1 if x==0 else 0)#cuento las cuentas abiertas
        filtrado=filtrado.replace("None",0)#limpio los none
        filtrado=filtrado.astype(str)
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].astype(str)
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].astype(str)
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].apply(lambda x: 0 if x=="" else x )
        filtrado['limiteDeCredito']=filtrado['limiteDeCredito'].astype(int)
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].astype(str)
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].astype(str)
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].apply(lambda x: 0 if x=="" else x )
        filtrado['creditoMaximo']=filtrado['creditoMaximo'].astype(int)
        filtrado['saldoActual']=filtrado['saldoActual'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['saldoActual']=filtrado['saldoActual'].astype(str)
        filtrado['saldoActual']=filtrado['saldoActual'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['saldoActual']=filtrado['saldoActual'].astype(str)
        filtrado['saldoActual']=filtrado['saldoActual'].apply(lambda x: 0 if x=="" else x )
        filtrado['saldoActual']=filtrado['saldoActual'].astype(int)
        filtrado['saldoVencido']=filtrado['saldoVencido'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['saldoVencido']=filtrado['saldoVencido'].astype(str)
        filtrado['saldoVencido']=filtrado['saldoVencido'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['saldoVencido']=filtrado['saldoVencido'].astype(str)
        filtrado['saldoVencido']=filtrado['saldoVencido'].apply(lambda x: 0 if x=="" else x )
        filtrado['saldoVencido']=filtrado['saldoVencido'].astype(int)
        filtrado['montoApagar']=filtrado['montoApagar'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['montoApagar']=filtrado['montoApagar'].astype(str)
        filtrado['montoApagar']=filtrado['montoApagar'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['montoApagar']=filtrado['montoApagar'].astype(str)
        filtrado['montoApagar']=filtrado['montoApagar'].apply(lambda x: 0 if x=="" else x )
        filtrado['montoApagar']=filtrado['montoApagar'].astype(int)
        filtrado['saldoMorosidadHistMasGrave']=filtrado['saldoMorosidadHistMasGrave'].apply(lambda x: (int(x[:-1])*-1) if x[-1]=="-" else x )
        filtrado['saldoMorosidadHistMasGrave']=filtrado['saldoMorosidadHistMasGrave'].astype(str)
        filtrado['saldoMorosidadHistMasGrave']=filtrado['saldoMorosidadHistMasGrave'].apply(lambda x: (int(x[:-1])*1) if x[-1]=="+" else x )
        filtrado['saldoMorosidadHistMasGrave']=filtrado['saldoMorosidadHistMasGrave'].astype(int)
        filtrado['saldoMorosidadHistMasGrave']=filtrado['saldoMorosidadHistMasGrave'].apply(lambda x: 0 if x=="" else x )
        
        fechas=filtrado.groupby(['cuentas']).agg({
            'updatedAt':lambda x: x.iloc[0]
        })
        
        
        df_cuentas_abiertas=filtrado.loc[:,['cuentas','cuentasAbiertas','limiteDeCredito','creditoMaximo','saldoActual','saldoVencido','saldoMorosidadHistMasGrave','montoApagar']]
        df_cuentas_abiertas['cuentasAbiertas']=df_cuentas_abiertas['cuentasAbiertas'].astype(int)
        df_cuentas_abiertas = df_cuentas_abiertas.drop(df_cuentas_abiertas[df_cuentas_abiertas['cuentasAbiertas'] == 0].index)
        df_cuentas_abiertas = df_cuentas_abiertas.groupby(['cuentas']).agg({
        'cuentasAbiertas':'sum',
        'limiteDeCredito':'sum',
        'creditoMaximo':'sum',
        'saldoActual':'sum',
        'saldoMorosidadHistMasGrave':'sum',
        'saldoVencido':'sum',
        'montoApagar':'sum'})
        df_cuentas_abiertas['cuentasCerradas']=0
        df_cuentas_abiertas.columns=['cuentas','cuentasAbiertas','limiteAbiertas','maximoAbiertos','saldoActualAbiertas','saldoVencidoAbiertas','pagar','cuentasCerradas']
    
        
        df_cuentas_cerradas=filtrado.loc[:,['cuentas','cuentasCerradas','limiteDeCredito','creditoMaximo','saldoActual','montoApagar']]
        df_cuentas_cerradas['cuentasCerradas']=df_cuentas_cerradas['cuentasCerradas'].astype(int)
        df_cuentas_cerradas = df_cuentas_cerradas.drop(df_cuentas_cerradas[df_cuentas_cerradas['cuentasCerradas'] == 0].index)
        df_cuentas_cerradas = df_cuentas_cerradas.groupby(['cuentas']).agg({
        'cuentasCerradas':'sum',
        'limiteDeCredito':'sum',
        'creditoMaximo':'sum',
        'saldoActual':'sum',
        'montoApagar':'sum'})
        df_cuentas_cerradas.columns=['cuentasCerradas','limiteCerradas','maximoCerradas','saldoActualCerradas','monte Cerradas']
        
        final = pd.concat([df_cuentas_abiertas, df_cuentas_cerradas])
        final["Actualizado en"]=fechas
        print(final)
        final=final[['cuentas','cuentasAbiertas','limiteAbiertas','maximoAbiertos','saldoActualAbiertas','saldoVencidoAbiertas','pagar','cuentasCerradas','limiteCerradas','maximoCerradas','saldoActualCerradas','monte Cerradas','Actualizado en']]
        final.to_parquet(f"rfc.parquet",engine="pyarrow")



       



resumen_creditos("b.xlsx","PF")
