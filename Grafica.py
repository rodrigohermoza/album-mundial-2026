from os import linesep

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from Constantes import total_figuras, Figuras_sobre,Precio_sobre, N_REPETICIONES, REFERENCIAS

#Colores para grafica (los eligio chat gpt porque no tengo ni idea de colores)

COLOR_FONDO        = "#0D1B2A"   # Azul muy oscuro
COLOR_CURVA        = "#FFD700"   # Dorado FIFA
COLOR_REFERENCIA   = "#FF6B6B"   # Rojo coral para líneas de referencia
COLOR_ANOTACION    = "#FFFFFF"   # Blanco para texto
COLOR_GRID         = "#1E3A5F"   # Azul medio para la cuadrícula

def graficar(sobres, porcentajes):
    #Es la grafica que muestra costo vs probabilidad de llenar el album
    #Necesita del array con el numero de sobres y el array de porcentajes acumulados
    costo_soles = sobres*Precio_sobre

    #Comenzamos con la figura

    fig, ax = plt.subplots(figsize = (13,7), dpi = 110)
    fig.patch.set_facecolor(COLOR_FONDO)
    ax.set_facecolor(COLOR_FONDO)

    #Curva principal
    ax.plot(costo_soles,porcentajes, color = COLOR_CURVA,
            linewidth = 2.5, zorder = 3, label = "Probabilidad Acumulada")
    ax.fill_between(costo_soles,porcentajes,alpha = 0.08, color = COLOR_CURVA, zorder = 2)

    #Referencias
    for pct in REFERENCIAS:
        idx = np.searchsorted(porcentajes,pct)
        idx = min(idx, len(costo_soles)-1)
        costo = costo_soles[idx]

        ax.axhline(y = pct, color = COLOR_REFERENCIA, linestyle = "--", linewidth = 0.8, alpha = 0.6,  zorder = 1)
        ax.axvline(x = costo, color = COLOR_REFERENCIA, linestyle = ":", linewidth = 0.8, alpha = 0.6, zorder = 1)
        ax.scatter(costo, pct, color = COLOR_REFERENCIA, s = 60, zorder = 5)
        ax.annotate(f" {pct}% → S/ {costo:,.0f}",xy = (costo,pct), xytext = (costo + max(costo_soles)*0.01, pct - 2.5),
                    color = COLOR_ANOTACION, fontsize = 8.5, fontweight = "bold", zorder = 6)

    #Ejes, titulos
    ax.set_xlabel("Dinero invesrtido en sobres", color = COLOR_ANOTACION, fontsize = 12, labelpad = 12)
    ax.set_ylabel("Probabilidad de haber encontrado el album", color = COLOR_ANOTACION, fontsize = 12, labelpad = 12)
    ax.set_title("Cuanto cuesta completar el Album del Mundial 2026", color = COLOR_CURVA, fontsize = 16, fontweight = "bold", pad = 20)

    #limites
    ax.set_ylim(0,103)
    #formatos de ejes
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"S/ {x:,.0f}"))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"{y:.0f}%"))

    ax.tick_params(colors=COLOR_ANOTACION, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor(COLOR_GRID)

    #Cuadricula
    ax.grid(True, color=COLOR_GRID, linestyle="--", linewidth=0.5, alpha=0.5)

    #informacion
    info = (
        f"Álbum: {total_figuras} figuritas\n"
        f"Sobre: {Figuras_sobre} figuritas · S/ {Precio_sobre:.2f}\n"
        f"Método: Monte Carlo (simulación)"
    )
    ax.text(0.02,0.97, info, transform = ax.transAxes, verticalalignment = "top",
    color = COLOR_ANOTACION, fontsize = 8, alpha = 0.75,
    bbox = dict(boxstyle = "round,pad=0.4", facecolor = "#1E3A5F", edgecolor = COLOR_GRID, alpha = 0.8))

    plt.tight_layout()
    plt.savefig("album_mundial_2026.png", dpi=150, bbox_inches="tight")
    plt.show()