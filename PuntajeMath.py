import pandas as pd

data = pd.read_csv('resultados.csv')


def estadisticas(data: pd.DataFrame) -> dict:
    nacional = data[['ESTU_MCPIO_RESIDE', 'PUNT_MATEMATICAS']]
    prom_nacional = nacional['PUNT_MATEMATICAS'].mean()
    bquilla = nacional[nacional.ESTU_MCPIO_RESIDE == 'BARRANQUILLA']
    prom_bquilla = bquilla['PUNT_MATEMATICAS'].mean()
    ofinotofi = data[['COLE_NATURALEZA', 'PUNT_MATEMATICAS']]
    oficiales = ofinotofi[ofinotofi.COLE_NATURALEZA == 'OFICIAL']
    noOficiales = ofinotofi[ofinotofi.COLE_NATURALEZA == 'NO OFICIAL']
    prom_ofi = oficiales['PUNT_MATEMATICAS'].mean()
    prom_notOfi = noOficiales['PUNT_MATEMATICAS'].mean()
    resul1 = None
    resul2 = None
    if (prom_ofi > prom_notOfi):
        resul1 = (prom_ofi, "Oficial")
    else:
        resul1 = (prom_notOfi, "No Oficial")

    if (prom_nacional > prom_bquilla):
        resul2 = (prom_nacional, "Nacional")
    else:
        resul2 = (prom_bquilla, "Local")
    diccionario = {
        'nacional_math': prom_nacional,
        'performance_math': resul2,
        'mejor_resultado': resul1
    }
    return print(diccionario)


estadisticas(data)
