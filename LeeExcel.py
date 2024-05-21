import pandas as pd
import random
datos = pd.read_excel("/Users/ezequieldubrowsky/Documents/programacion/Repos/JuicioPorJuradoInfo/alumnosfilas.xlsx")
filas_como_dict = datos.to_dict(orient='records')

# Imprime las filas como diccionarios (opcional)
for fila_dict in filas_como_dict:
    print(fila_dict)


def ImportarDatos():
    pass
def Seleccion():
    pass