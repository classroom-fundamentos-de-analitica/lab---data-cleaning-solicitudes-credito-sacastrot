"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)
    df=df.drop(['Unnamed: 0'], axis=1)
    df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]]=df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    df=df.replace(to_replace="(_)|(-)",value=" ",regex=True)    
    df=df.replace(to_replace="[,$]|(\.00$)",value="",regex=True)
    df.monto_del_credito = df.monto_del_credito.astype("int")
    df.comuna_ciudadano = df.comuna_ciudadano.astype("float")
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,infer_datetime_format=True,errors='ignore',dayfirst=True)
    df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime("%Y/%m/%d")
    df.drop_duplicates(inplace = True)

    return df