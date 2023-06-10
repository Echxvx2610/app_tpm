import pandas as pd

linea_1 = pd.read_csv(r'LINEA 1/Datos Operadores.csv')
df = pd.DataFrame(linea_1)
print(df,'\n')
print(df["Nombre"],'\n')
