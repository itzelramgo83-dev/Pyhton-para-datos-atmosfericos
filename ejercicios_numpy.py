
import numpy as np


# ================================================================
#  NIVEL 1 — Crear y manipular arrays
# ================================================================
#  Lo más básico: cómo crear arrays y hacer operaciones con ellos.
#  Un array de NumPy es como una lista de Python pero más rápido
#  y con operaciones matemáticas elemento a elemento.
# ================================================================

print("=" * 60)
print("NIVEL 1 — Crear y manipular arrays")
print("=" * 60)

# ---------------------------------------------------------------
#  1.1) Crea un array con las temperaturas de una semana:
#       [22, 25, 19, 30, 28, 21, 24]
#       Calcula la media, el máximo y el mínimo.
# ---------------------------------------------------------------

temp= np.array([22, 25, 19, 30, 28, 21, 24])
print("Media:", np.mean(temp))
print("Máximo:", np.max(temp))
print("Mínimo:", np.min(temp))
# ---------------------------------------------------------------
#  1.2) Crea un array de alturas de 0 a 5000 metros, cada 500 m.
#       Usa np.arange.
#       ¿Cuántos elementos tiene?
# ---------------------------------------------------------------

# np.arange(inicio, fin, paso) — OJO: el fin NO se incluye,
# por eso ponemos 5500 si queremos que llegue a 5000.


alturas = np.arange(0, 5500, 500)
print("Elementos en alturas:", len(alturas))

# ---------------------------------------------------------------
#  1.3) Crea un array de 10 valores equidistantes entre 0 y 100.
#       Usa np.linspace.
# ---------------------------------------------------------------

# np.linspace(inicio, fin, cantidad) — aquí sí INCLUYE el fin.
# Es diferente de arange: le dices cuántos puntos quieres,
# no el paso.

array= np.linspace(0, 100, 10)
print("Array de 10 valores equidistantes:", array)

# ---------------------------------------------------------------
#  1.4) Operaciones elemento a elemento.
#       Tienes temperaturas en Celsius: [0, 20, 37, 100]
#       Conviértelas a Fahrenheit:  F = C * 9/5 + 32
#       y a Kelvin:  K = C + 273.15
# ---------------------------------------------------------------
# En NumPy las operaciones se aplican a TODOS los elementos
# automáticamente. No necesitas un for loop.

C= np.array([0,20,37,100])
F = C * 9/5 + 32
K = C + 273.15

print("Temperaturas en Celsius:", C)
print("Temperaturas en Fahrenheit:", F)
print("Temperaturas en Kelvin:", K)

# ---------------------------------------------------------------
#  1.5) Crea un array de 8 ceros y otro de 5 unos.
#       Usa np.zeros y np.ones.
# ---------------------------------------------------------------

ceros = np.zeros(8)
unos = np.ones(5)

print("Array de 8 ceros:", ceros)
print("Array de 5 unos:", unos)

# ================================================================
#  NIVEL 2 — Indexing y slicing
# ================================================================
#  Cómo seleccionar partes de un array.
#  Es igual que listas de Python pero con más poderes.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 2 — Indexing y slicing")
print("=" * 60)

# ---------------------------------------------------------------
#  2.1) Dado este array de presiones (hPa):
#       [1013, 950, 850, 700, 500, 300, 200, 100]
#       Obtén: el primer elemento, el último, los 3 primeros,
#       y los 3 últimos.
# ---------------------------------------------------------------

presion = np.array([1013, 950, 850, 700, 500, 300, 200, 100])
print("Primer elemento:", presion[0])
print("Último elemento:", presion[-1])
print("Tres primeros elementos:", presion[:3])
print("Tres últimos elementos:", presion[-3:])
# ---------------------------------------------------------------
#  2.2) Del mismo array, obtén los elementos en posiciones pares
#       (0, 2, 4, 6) usando slicing con paso.
# ---------------------------------------------------------------

# array[inicio:fin:paso]

slicing= presion[0:8:2] 
print("Elementos en posiciones pares:", slicing)
# ---------------------------------------------------------------
#  2.3) Modifica el array: cambia el valor en la posición 3
#       de 700 a 750. Luego cambia los dos últimos a 999.
# ---------------------------------------------------------------
presion_copia = presion.copy()   # hacemos copia para no perder el original
presion_copia[3] = 750
presion_copia[-2:] = 999
print("Array modificado:", presion_copia)
# ---------------------------------------------------------------
#  2.4) Tienes un array de 12 meses de lluvia (mm):
#       Obtén solo los meses de verano (junio=5, julio=6, agosto=7)
#       usando una lista de índices.
# ---------------------------------------------------------------
# "Fancy indexing": pasas una lista de índices y te devuelve
# los elementos en esas posiciones.

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])

verano = lluvia[[5, 6, 7]]
print("Lluvia en verano:", verano)

# ================================================================
#  NIVEL 3 — Máscaras booleanas
# ================================================================
#  ESTE ES EL CONCEPTO MÁS IMPORTANTE para los ejercicios
#  de atmósfera. Una máscara es un array de True/False que
#  usas para filtrar datos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 3 — Máscaras booleanas")
print("=" * 60)

# ---------------------------------------------------------------
#  3.1) Tienes temperaturas de 10 días:
#       Crea una máscara que sea True donde T > 25.
#       Úsala para obtener solo las temperaturas calientes.
# ---------------------------------------------------------------
T=np.array([22, 25, 19, 30, 28, 21, 24, 26, 27, 23])
mascara_caliente = T > 25
temperaturas_calientes = T[mascara_caliente]
print("Temperaturas calientes:", temperaturas_calientes)

# ---------------------------------------------------------------
#  3.2) Combina condiciones: selecciona temperaturas entre 20 y 28
#       (inclusive). Usa & (and) con paréntesis.
# ---------------------------------------------------------------

# IMPORTANTE: cada condición va entre paréntesis cuando usas & o |
# & : and (ambas deben ser True)
# | : or  (al menos una debe ser True)
# ~ : not (invierte True/False)

Condiciones= (T >= 20) & (T <= 28)
temperaturas_20_28 = T[Condiciones]
print("Temperaturas entre 20 y 28:", temperaturas_20_28)

# ---------------------------------------------------------------
#  3.3) ¿Cuántos días fueron calientes (T > 25)?
#       Usa np.sum sobre la máscara.
# ---------------------------------------------------------------
# True se cuenta como 1, False como 0.
# Entonces np.sum de una máscara = cantidad de True.
dias_calientes = np.sum(mascara_caliente)
print("Número de días calientes:", dias_calientes)

# ---------------------------------------------------------------
#  3.4) Reemplaza valores: pon 0 donde la temperatura sea menor
#       a 22 (simular que no hubo evento significativo).
# ---------------------------------------------------------------

T[T < 22] = 0
print("Temperaturas remplazadas:", T)

# ---------------------------------------------------------------
#  3.5) Clasificación con máscaras: clasifica cada temperatura
#       como "fría" (<22), "templada" (22-28), o "caliente" (>28).
#       Cuenta cuántas hay de cada clase.
# ---------------------------------------------------------------

Temp_fria= np.sum(T < 22)
Temp_templada= np.sum((T >= 22) & (T <= 28))
Temp_caliente= np.sum(T > 28)
print("Cantidad de días fríos:", Temp_fria)
print("Cantidad de días templados:", Temp_templada)
print("Cantidad de días calientes:", Temp_caliente)

# ---------------------------------------------------------------
#  3.6) np.where: encuentra los ÍNDICES donde se cumple una
#       condición. ¿En qué días (posiciones) llovió más de 80 mm?
# ---------------------------------------------------------------

lluvia = np.array([30, 25, 40, 60, 80, 120, 150, 140, 90, 50, 35, 28])

# np.where devuelve una TUPLA. El [0] saca el array de índices.
# ¿Por qué tupla? Porque en 2D devolvería (filas, columnas).
# En 1D solo hay un eje, pero la tupla siempre está.

where= np.where(lluvia > 80)[0]
print("Días con lluvia > 80 mm (índices):", where)  
# ================================================================
#  NIVEL 4 — Funciones útiles: diff, cumsum, nan
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 4 — diff, cumsum y NaN")
print("=" * 60)

# ---------------------------------------------------------------
#  4.1) np.diff: diferencias consecutivas.
#       Tienes alturas de un globo cada minuto:
#       [100, 250, 430, 600, 590, 610, 800]
#       Calcula cuánto subió (o bajó) entre cada minuto.
# ---------------------------------------------------------------

# np.diff calcula elemento[i+1] - elemento[i].
# Si hay N elementos, el resultado tiene N-1 elementos.

print("Alturas del globo:", [100, 250, 430, 600, 590, 610, 800])
alturas_globo = np.array([100, 250, 430, 600, 590, 610, 800])
diferencias = np.diff(alturas_globo)
print("Diferencias entre minutos:", diferencias)    
print("ESTE NO LO VIMOS") 
# ---------------------------------------------------------------
#  4.2) np.cumsum: suma acumulada.
#       Tienes lluvia horaria (mm): [2, 5, 0, 1, 8, 3, 0]
#       Calcula la lluvia acumulada a cada hora.
# ---------------------------------------------------------------
# cumsum: [2, 2+5, 2+5+0, 2+5+0+1, ...] = [2, 7, 7, 8, 16, 19, 19]

lluvia_acumulada = np.array([2, 5, 0, 1, 8, 3, 0])
acumulada = np.cumsum(lluvia_acumulada)
print("Lluvia acumulada:", acumulada)

# ---------------------------------------------------------------
#  4.3) NaN: datos faltantes.
#       Tienes mediciones con huecos (sensor falló):
#       [22.5, nan, 23.1, 24.0, nan, nan, 22.8]
#       Calcula la media ignorando los NaN.
# ---------------------------------------------------------------

# np.nan es un valor especial = "no hay dato".
# np.mean falla con NaN (da NaN). Usa np.nanmean.
array= np.array([22.5, np.nan, 23.1, 24.0, np.nan, np.nan, 22.8])
media_sinNAN= np.nanmean(array)
print("Media ignorando NaN:", media_sinNAN)


# ---------------------------------------------------------------
#  4.4) Detectar y contar NaN.
# ---------------------------------------------------------------

nan_indices = np.where(np.isnan(array))[0]
print("Índices de NaN:", nan_indices)
print("Cantidad de NaN:", len(nan_indices))
print("NO LO VIMOS TAMPOCO CREO")
# ---------------------------------------------------------------
#  4.5) Reemplazar valores malos con NaN.
#       Un sensor marca -999 cuando falla. Límpialo.
# ---------------------------------------------------------------
datos_fallos=np.array([22.5, -999, 23.1, 24.0, -999, -999, 22.8])
limpio= np.where(datos_fallos == -999, np.nan, datos_fallos)
print("Array limpio de -999:", limpio)
# ---------------------------------------------------------------
#  4.6) Limpieza combinada: reemplaza valores negativos Y
#       mayores a 100 con NaN (outliers de un sensor de humedad).
# ---------------------------------------------------------------

humedad = np.array([55, 72, -5, 88, 150, 63, -10, 91, 200, 45])
humedad_limpia = humedad.astype(float)  # necesario para poder poner NaN

limpieza = np.where((humedad_limpia < 0) | (humedad_limpia > 100), np.nan, humedad_limpia)
print("Humedad limpia de outliers:", limpieza)

# ================================================================
#  NIVEL 5 — Arrays 2D y operaciones por eje
# ================================================================
#  En meteorología casi siempre trabajas con datos 2D o más:
#  (estaciones × tiempo), (latitud × longitud), etc.
#  Entender los ejes es CLAVE.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 5 — Arrays 2D y ejes")
print("=" * 60)

# ---------------------------------------------------------------
#  5.1) Crea una matriz de temperaturas: 3 estaciones × 5 días.
#       Cada fila es una estación, cada columna es un día.
# ---------------------------------------------------------------

temperaturas = np.array([[20, 22, 24, 26, 28],
                        [18, 20, 22, 24, 26],
                        [16, 18, 20, 22, 24]])
print("Matriz de temperaturas (estaciones × días):")
print(temperaturas)
# ---------------------------------------------------------------
#  5.2) Promedios por eje.
#       axis=0: promedia "hacia abajo" (sobre las estaciones)
#               → te da un promedio por día
#       axis=1: promedia "hacia la derecha" (sobre los días)
#               → te da un promedio por estación
# ---------------------------------------------------------------

# TRUCO para recordar: axis=X elimina esa dimensión.
#   axis=0 → elimina filas → queda un valor por columna
#   axis=1 → elimina columnas → queda un valor por fila

promedio_por_dia = np.mean(temperaturas, axis=0)
promedio_por_estacion = np.mean(temperaturas, axis=1)

print("Promedio por día:", promedio_por_dia)
print("Promedio por estación:", promedio_por_estacion)

# ---------------------------------------------------------------
#  5.3) Máximo y mínimo por eje.
# ---------------------------------------------------------------
max_por_dia = np.max(temperaturas, axis=0)
min_por_estacion = np.min(temperaturas, axis=1)
print("Máximo por día:", max_por_dia)
print("Mínimo por estación:", min_por_estacion) 

# ---------------------------------------------------------------
#  5.4) Máscaras en 2D.
#       Encuentra todas las celdas donde T > 25.
# ---------------------------------------------------------------
mascara_T_mayor_25 = temperaturas > 25
print("Máscara de T > 25:", mascara_T_mayor_25)

# ---------------------------------------------------------------
#  5.5) np.where en 2D.
#       Devuelve DOS arrays: filas y columnas.
# ---------------------------------------------------------------
dos_d =np.where(temperaturas > 25)
print("Filas donde T > 25:", dos_d[0])
print("Columnas donde T > 25:", dos_d[1])  


# ---------------------------------------------------------------
#  5.6) Seleccionar filas y columnas específicas.
# ---------------------------------------------------------------

# Una fila completa (estación B):
# Una columna completa (día 3):
# Un bloque (estaciones A y B, días 1 a 3):

Estación_b= temperaturas[1, :]
Día_3= temperaturas[:, 2]
Bloque= temperaturas[0:2, 0:3]

# ================================================================
#  NIVEL 6 — Reshape y broadcasting
# ================================================================
#  Reshape cambia la forma de un array sin cambiar los datos.
#  Broadcasting permite operar arrays de distinto tamaño.
#  Ambos se usan MUCHO en datos atmosféricos.
# ================================================================

print("\n\n" + "=" * 60)
print("NIVEL 6 — Reshape y broadcasting")
print("=" * 60)

# ---------------------------------------------------------------
#  6.1) Reshape básico.
#       Tienes 24 mediciones horarias en un array 1D.
#       Reorganízalas en una matriz de 4 periodos × 6 horas.
# ---------------------------------------------------------------

# reshape no cambia los datos, solo la forma del array.
# El total de elementos debe coincidir: 24 = 4 × 6

matriz_4x6 = np.arange(24).reshape(4, 6)
print("Matriz 4 periodos × 6 horas:", matriz_4x6)

# ---------------------------------------------------------------
#  6.2) Reshape para promedios por periodo.
#       Tienes 30 días × 24 horas = 720 datos de temperatura.
#       Calcula el promedio diario.
# ---------------------------------------------------------------

# Simulamos 720 horas de datos
np.random.seed(42)
temp_horaria = 20 + 5 * np.sin(2 * np.pi * np.tile(np.arange(24), 30) / 24) \
               + np.random.normal(0, 1, 720)

# Reshape a (30 días, 24 horas) y promediamos sobre las horas

reshape= temp_horaria.reshape(30, 24)
promedio_diario = np.mean(reshape, axis=1)
print("Promedio diario de temperatura:", promedio_diario)

# ---------------------------------------------------------------
#  6.3) Broadcasting: operaciones entre arrays de distinto tamaño.
#       NumPy "estira" el array más chico para que coincida.
# ---------------------------------------------------------------

# Ejemplo simple: restar la media de cada columna a una matriz.
# La matriz es (3, 5) y la media por columna es (5,).
# NumPy automáticamente resta cada media a su columna.

matriz_1 = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15]])
media_columna = np.mean(matriz_1, axis=0)
resta = matriz_1 - media_columna
print("Matriz original:\n", matriz_1)
print("Media por columna:", media_columna)
print("Matriz después de restar la media por columna:\n", resta)

# ---------------------------------------------------------------
#  6.4) Broadcasting con None (np.newaxis).
#       A veces necesitas agregar un eje para que el broadcasting
#       funcione en la dirección correcta.
# ---------------------------------------------------------------

# Si quieres restar la media por FILA (no columna):

# Esto falla: datos(3,3) - media_fila(3,) resta por columna, no fila.
# Necesitas convertir media_fila de shape (3,) a shape (3, 1):


media_fila = np.mean(matriz_1, axis=1)  # shape (3,)
media_fila_reshaped = media_fila[:, np.newaxis]  # shape (3, 1)
resta_fila = matriz_1 - media_fila_reshaped
print("Media por fila:", media_fila)
print("Matriz después de restar la media por fila:\n", resta_fila)

# ---------------------------------------------------------------
#  6.5) Ejemplo atmosférico: calcular anomalías mensuales.
#       Tienes 3 años × 12 meses de temperatura.
#       Calcula la climatología (promedio de cada mes) y resta.
# ---------------------------------------------------------------

# Simulamos datos: 3 años × 12 meses
# Climatología: promedio de cada mes sobre los 3 años
# Anomalías: cada año menos la climatología
# Broadcasting funciona directo: (3, 12) - (12,)


datos_simulados= 15 + 10 * np.random.rand(3, 12)  # 3 años × 12 meses
climatologia = np.mean(datos_simulados, axis=0)  # shape (12,)
anomalías = datos_simulados - climatologia  # broadcasting resta (3,12)
print("Datos simulados (3 años × 12 meses):\n", datos_simulados)
print("Climatología (promedio por mes):", climatologia)
print("Anomalías (cada año menos la climatología):\n", anomalías)

