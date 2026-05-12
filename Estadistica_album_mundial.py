#Proyecto para ver cuanto costaría llenar el album del mundial
#Esto será en medido con porcentajes de probabilidad
#Sabemos que hay 980 stickers del mundial y 7 stickers por sobre
#El sobre cuesta 4.20

from Simulacion import correr_simulacion, calcular_porcentajes
from Grafica    import graficar

def main():
    print("=" * 50)
    print("  SIMULADOR - ÁLBUM MUNDIAL 2026 ")
    print("=" * 50)

    #Corremos la simulacion
    resultados = correr_simulacion()
    sobres,porcentajes = calcular_porcentajes(resultados)
    graficar(sobres,porcentajes)
if __name__ == "__main__":
    main()