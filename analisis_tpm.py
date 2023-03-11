import pandas as pd

linea_1 = pandas.read_csv(r'LINEA 1\Datos Operadores.csv')
df = pandas.DataFrame(linea_1)
print(df)