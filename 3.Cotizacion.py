import pandas as pd
def resumen_cotizaciones(nombre_archivo):
    df = pd.read_csv(nombre_archivo)

    #calculamos el mínimo, el máximo y la media de cada columna
    resumen = {
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Media': df.mean()
    }

    #creamos un dataframe a partir del resumen
    resumen_df = pd.DataFrame(resumen)

    return resumen_df


archivo = 'cotizacion.csv'
resumen = resumen_cotizaciones(archivo)

# Muestra el DataFrame con el mínimo, el máximo y la media de cada columna
print(resumen)
