# Resumen de Algoritmos
## 1. Búsqueda en Anchura (BFS) – 8 Puzzle
Se implementó el algoritmo Breadth-First Search (BFS) para resolver el rompecabezas clásico del 8-Puzzle. Este algoritmo explora los estados por niveles, utilizando una cola y un registro de estados visitados para evitar ciclos. Su ventaja principal es que garantiza siempre la solución óptima en el menor número de movimientos.

## 2. Problemas de Transición de Estados
Se desarrollaron dos ejemplos simples para ilustrar el concepto de transición de estados:
Mascota triste: el estado cambia de "triste" a "contenta" mediante la acción de dar comida.
Tesoro del pirata: un pirata parte de la posición inicial en una cuadrícula y avanza con acciones válidas hasta alcanzar la meta (el tesoro).
Estos casos muestran cómo los agentes pueden reaccionar de forma determinística para alcanzar un objetivo definido.

## 3. Resolución de Laberinto con Obstáculos
Se diseñó un sistema que combina dos modos de operación:
Manual: el usuario ingresa los movimientos hasta intentar llegar a la meta.
Automático: si el usuario no alcanza el objetivo, se activa un algoritmo BFS que encuentra el camino más corto evitando obstáculos.
Este enfoque híbrido refleja la integración de la interacción humana con la resolución sistemática de un agente inteligente.
