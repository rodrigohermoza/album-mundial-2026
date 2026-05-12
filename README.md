# 🏆 Simulador de Costo — Álbum Panini Mundial 2026

¿Cuánta plata necesitas para completar el álbum del Mundial 2026?  
Este proyecto responde esa pregunta con **simulación Monte Carlo** y una gráfica interactiva.

---

## 📊 ¿Qué hace el programa?

Simula miles de veces el proceso de comprar sobres del álbum Panini hasta completarlo, y genera una gráfica que muestra:

> **"Si invierto S/ X en sobres, ¿qué probabilidad tengo de haber completado el álbum?"**

El resultado es una curva de probabilidad acumulada (CDF) que te dice, por ejemplo:
- Con **S/ X** tienes un 50% de probabilidad de completarlo
- Con **S/ Y** tienes un 90% de probabilidad
- Con **S/ Z** tienes un 99% de probabilidad

---

## 🧠 ¿Cómo funciona?

El problema de completar un álbum de figuritas es una versión del clásico **Coupon Collector's Problem** de probabilidad. No tiene una fórmula cerrada simple para porcentajes arbitrarios, por eso se resuelve con simulación.

**Pasos del algoritmo:**

1. Se crea un `set` vacío que representa el álbum (los sets ignoran duplicados, igual que un álbum real)
2. Se "compran" sobres en un loop, agregando figuritas aleatorias al set
3. El loop termina cuando el set tiene las 980 figuritas únicas
4. Se repite este experimento **5,000 veces**
5. Con los resultados se construye la curva de probabilidad acumulada

---

## 📁 Estructura del proyecto

```
album_mundial/
│
├── estadistica_album_mundial.py          # Punto de entrada — orquesta todo el programa
├── simulacion.py    # Lógica Monte Carlo (simular_album, calcular_cdf)
├── grafica.py       # Visualización con matplotlib
└── constantes.py    # Parámetros del álbum (figuritas, precio, etc.)
```

---

## 🚀 Cómo ejecutarlo

### 1. Instalar dependencias

```bash
pip install numpy matplotlib
```

### 2. Ejecutar

```bash
python main.py
```

La simulación tarda aproximadamente **30–60 segundos** dependiendo de tu equipo.  
Al terminar se abre automáticamente la gráfica.

---

## ⚙️ Configuración

Puedes ajustar los parámetros del álbum editando `constantes.py`:

```python
total_figuras = 980      # Figuritas únicas del álbum
Figuras_sobre = 7        # Figuritas por sobre
Precio_sobre  = 4.20     # Precio en Soles (Perú)
N_REPETICIONES    = 5_000    # Más simulaciones = más precisión
```

---

## 📦 Dependencias

| Librería | Uso |
|---|---|
| `numpy` | Generación de figuritas aleatorias y operaciones sobre arrays |
| `matplotlib` | Graficación de la curva de probabilidad |

---

## 📷 Ejemplo de gráfica

La gráfica muestra la curva en color dorado sobre fondo oscuro, con líneas de referencia en los porcentajes clave (50%, 75%, 90%, 95%, 99%) y el costo en soles correspondiente a cada uno.

---

## 💡 Posibles mejoras

- [ ] Simular el efecto de intercambiar figuritas con amigos
- [ ] Comparar con el costo de comprar las figuritas faltantes individualmente  
- [ ] Agregar segunda curva en dólares (USD)
- [ ] Interfaz gráfica con parámetros ajustables en tiempo real

---

Hecho con Python 🐍 | Datos basados en el álbum Panini oficial del Mundial 2026
