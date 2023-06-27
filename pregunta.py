"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df = df.drop('Unnamed: 0', axis = 1)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)  #formato de fecha estandarizado

    df['monto_del_credito'] = df['monto_del_credito'].map(lambda x: str(x).strip('$').replace(',','')) #estandarizando el formato de dinero
    df.monto_del_credito = df.monto_del_credito.astype(float)   #No deja convertir a int, entonces primero convierto a float
    df.monto_del_credito = df.monto_del_credito.astype(int)   #Luego a int

    #las columnas de strings pasandolas a minuscula y cambiando - y _ por espacios en blanco
    df[['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']] = df[['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']].applymap(lambda s: s.lower().replace('-',' ').replace('_',' ') if type(s) == str else s)

    #dropeo de nulos y duplicados
    df.dropna(axis=0, inplace = True)
    df.drop_duplicates(inplace=True)

    return df