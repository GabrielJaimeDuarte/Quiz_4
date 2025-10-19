```markdown
# Problema del Agente Viajero - Solución con Algoritmo Genético

## Descripción
Este proyecto implementa un algoritmo genético para resolver el Problema del Agente Viajero (TSP). El algoritmo encuentra la ruta más corta posible que visita cada ciudad exactamente una vez y regresa a la ciudad de origen.

## Definición del Problema
Dado un conjunto de ciudades con coordenadas, el TSP requiere encontrar el ciclo hamiltoniano más corto que visite cada ciudad exactamente una vez y regrese al punto de inicio.

## Coordenadas de las Ciudades
- A: (0, 0)
- B: (1, 5)
- C: (2, 3)
- D: (5, 2)
- E: (6, 6)
- F: (7, 1)
- G: (8, 4)
- H: (9, 9)

## Componentes del Algoritmo

### Cálculo de Distancias
- Distancia euclidiana entre ciudades
- Cálculo de distancia total de la ruta

### Operadores Genéticos
- **Inicialización**: Permutación aleatoria de ciudades
- **Selección**: Selección por torneo (tamaño 3)
- **Cruce**: Cruce ordenado (OX)
- **Mutación**: Mutación por intercambio con probabilidad 0.1

### Parámetros
- Tamaño de población: 50
- Generaciones: 100
- Tasa de mutación: 0.1

## Uso
Ejecuta el script de Python para ejecutar el algoritmo genético:

```bash
Quiz_4.py
```

El algoritmo mostrará:
- La mejor ruta encontrada
- La distancia total de la ruta óptima

## Salida
```
Mejor ruta encontrada: H -> G -> F -> D -> A -> C -> B -> E -> H
Distancia total: 31.07
```

## Requisitos
- Python 3.x
- Librerías estándar: random, math
