import random
import math

ciudades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (2, 3),
    'D': (5, 2),
    'E': (6, 6),
    'F': (7, 1),
    'G': (8, 4),
    'H': (9, 9)
}

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def distancia_ruta(ruta):
    total = 0
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        ciudad_siguiente = ciudades[ruta[(i+1) % len(ruta)]]
        total += distancia(ciudad_actual, ciudad_siguiente)
    return total

def crear_poblacion_inicial(tam_poblacion):
    ciudades_lista = list(ciudades.keys())
    poblacion = []
    for _ in range(tam_poblacion):
        ruta = ciudades_lista.copy()
        random.shuffle(ruta)
        poblacion.append(ruta)
    return poblacion

def seleccion(poblacion, distancias):
    torneo = random.sample(list(zip(poblacion, distancias)), 3)
    return min(torneo, key=lambda x: x[1])[0]

def cruce(padre1, padre2):
    start, end = sorted(random.sample(range(len(padre1)), 2))
    hijo = [None] * len(padre1)
    hijo[start:end] = padre1[start:end]
    
    pos = end
    for gen in padre2:
        if gen not in hijo:
            if pos >= len(hijo):
                pos = 0
            hijo[pos] = gen
            pos += 1
    return hijo

def mutacion(ruta, tasa_mutacion):
    if random.random() < tasa_mutacion:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

tam_poblacion = 50
generaciones = 100
tasa_mutacion = 0.1

poblacion = crear_poblacion_inicial(tam_poblacion)

for generacion in range(generaciones):
    distancias = [distancia_ruta(ruta) for ruta in poblacion]
    
    nueva_poblacion = []
    for _ in range(tam_poblacion):
        padre1 = seleccion(poblacion, distancias)
        padre2 = seleccion(poblacion, distancias)
        hijo = cruce(padre1, padre2)
        hijo = mutacion(hijo, tasa_mutacion)
        nueva_poblacion.append(hijo)
    
    poblacion = nueva_poblacion

mejor_ruta = min(poblacion, key=distancia_ruta)
mejor_distancia = distancia_ruta(mejor_ruta)

print(f"Mejor ruta encontrada: {' -> '.join(mejor_ruta)} -> {mejor_ruta[0]}")
print(f"Distancia total: {mejor_distancia:.2f}")
