#Script encuentro dos cuerpos mru
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sympy import symbols, Eq, solve

# Definir la variable t para SymPy
t = symbols('t')

# Definir las ecuaciones de movimiento
x1 = 35 * t
x2 = 1000 - 20 * t

# Posibles soluciones (x1=x2)
equation = Eq(x1, x2)
soluciones = solve(equation, t)
print(f'Las soluciones posibles son {soluciones}')

# Solución problema
encuentro_t = float(soluciones[0])
encuentro_x = 35 * encuentro_t

print(f'El tiempo de encuentro es {encuentro_t:.2f} segundos')
print(f'El lugar de encuentro es {encuentro_x:.2f} metros')

# Definir parámetros del movimiento
t_max = 30  # Tiempo máximo (s)
dt = 1      # Intervalo de tiempo (s)

# Crear el array de tiempos
ti = np.arange(0, t_max + dt, dt)

# Evaluar las ecuaciones de movimiento usando el array de tiempos
x1 = 35 * ti
x2 = 1000 - 20 * ti

# Crear una tabla con Pandas
tabla = pd.DataFrame({'Tiempo (s)': ti, 'Posición Cuerpo 1 (m)': x1, 'Posición Cuerpo 2 (m)': x2})
print(tabla)
