"""
ANÁLISIS DE SCOUTING: DELANTEROS MÁS LETALES - LA LIGA
Autor: DJimenez71
Fecha: 6 de Noviembre 2026
Descripción: Este script carga un dataset de'Football Players Stats 2026-2027' de Kaggle 
(recopilados originalmente de FBref).", filtra a los delanteros de La Liga con más de 
300 minutos jugados, y calcula su eficiencia (Goles/Tiro). Finalmente, genera un gráfico 
de dispersión para visualizar volumen vs eficiencia.
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- 1. CARGA DE DATOS ---
# Se asume que el archivo está en la carpeta 'archive/' respecto a este script.
RUTA_DATOS = 'archive/players_data-2026_2027.csv'
df = pd.read_csv(RUTA_DATOS)

# --- 2. FILTRADO Y LIMPIEZA ---
# Filtramos: Delanteros (FW), de la Liga Española ('es La Liga'), con > 300 min.
# Usamos variables intermedias para que el código sea más legible.
delanteros = df[
    (df['Min'] > 300) & 
    (df['Pos'] == 'FW') & 
    (df['Comp'] == 'es La Liga')
]

# --- 3. CÁLCULO DE MÉTRICAS ---
# Seleccionamos columnas clave: Jugador, Equipo, Goles, Tiros, Eficiencia (G/Sh) y Volumen (Sh/90).
# Ordenamos de mayor a menor eficiencia y tomamos el Top 10.
columnas_clave = ['Player', 'Squad', 'Gls', 'Sh', 'G/Sh', 'Sh/90']
top_letal = delanteros.sort_values(by='G/Sh', ascending=False).head(10)

print("\n--- TOP 10 DELANTEROS MÁS LETALES ---")
print(top_letal[columnas_clave])

# --- 4. VISUALIZACIÓN (GRÁFICO DE DISPERSIÓN) ---
# Creamos un gráfico donde el Eje X es el volumen de tiro (Sh/90) y el Eje Y la eficiencia (G/Sh).
plt.figure(figsize=(10, 6))
plt.scatter(top_letal['Sh/90'], top_letal['G/Sh'], color='blue', s=100)

# Iteramos sobre las filas para añadir el nombre de cada jugador al lado de su punto.
for i, row in top_letal.iterrows():
    plt.annotate(
        row['Player'], 
        (row['Sh/90'], row['G/Sh']),
        xytext=(5, 5), 
        textcoords='offset points', 
        fontsize=9
    )

# Personalización del gráfico
plt.title('Mapa de Letalidad: Volumen de Tiros vs Eficiencia (La Liga)')
plt.xlabel('Tiros por 90 minutos (Sh/90)')
plt.ylabel('Goles por Disparo (G/Sh)')
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()