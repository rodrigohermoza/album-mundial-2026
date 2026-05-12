import numpy as np
from Constantes import total_figuras, Figuras_sobre, Precio_sobre, N_REPETICIONES

#Para empezar la simulacion usaremos sets, que son como listas
#Pero estos solo guardan de forma tal que no se repitan, por ejemplo {1,2,4,5,4,6} se guardaria como {1,2,4,5,6}
#Las figuritas se enumeran del 1 al 980
#Por tanto se puede comprar figuritas en loop
#Hace sentido hacer una función que compre un sobre y agregue esas figuritas a un set; hasta terminar de llenar el album
#Esa sería la simulación numero 1, para ello hay otra función para hacer varias de esas simulaciones (x numero de simulaciones)

def simular_llenar_album():
    album = set()
    sobres_comprados = 0
    while len(album) < total_figuras:
        sobre = np.random.randint(1, total_figuras+1, size=Figuras_sobre)

        album.update(sobre)
        sobres_comprados += 1
    return sobres_comprados

def correr_simulacion():
    print(f"Corriendo {N_REPETICIONES} simulaciones")
    resultados = [simular_llenar_album() for _ in range(N_REPETICIONES)]
    #vamos a convertirlo en un array
    resultados = np.array(resultados)

    print("Estadistica de resultados")
    print(f"Mínimo de sobres necesario: {resultados.min()}")
    print(f"Máximo de sobres necesario: {resultados.max()}")
    print(f"Promedio de sobres necesario: {resultados.mean()}")
    print(f"Mediana de sobres necesario: {np.median(resultados)}")

    return resultados

def calcular_porcentajes(resultados):
    #calculamos los porcentajes acumulados de que rellenes el album
    #ya que al comprar más sobres, mayores son las probabilidades de llenar el album
    sobres_ordenados = np.sort(resultados)
    n =len(sobres_ordenados)
    porcentajes = np.arange(1,n+1)/n*100
    return sobres_ordenados, porcentajes

