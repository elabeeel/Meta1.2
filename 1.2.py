import pandas as pd
data = {
    'mes': ['enero', 'febrero', 'marzo', 'abril'],
    'ventas': [30500, 35600, 28300, 33900],
    'gastos': [22000, 23400, 18100, 20700]
}
df = pd.DataFrame(data)

print(df)

def calcular_balance_total(df, meses):
    balance_total = 0
    for index, row in df.iterrows():
        if row['mes'] in meses:
            balance_total += row['ventas'] - row['gastos']
    return balance_total


meses_interes = ['enero', 'marzo', 'abril']
balance = calcular_balance_total(df, meses_interes)
print(f'Balance total para los meses {", ".join(meses_interes)}: {balance}')


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
