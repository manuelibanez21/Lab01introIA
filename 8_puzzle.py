from collections import deque

# Estado final deseado
estado_final = [[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5]]

# Estado inicial
estado_inicial = [[2, 8, 3],
                  [1, 6, 4],
                  [7, 0, 5]]

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para encontrar la posición del cero (espacio vacío)
def encontrar_vacio(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                return i, j

# Función para convertir lista en tupla (hashable)
def a_tupla(tablero):
    return tuple(tuple(fila) for fila in tablero)

# BFS para resolver el puzzle
def bfs(estado_inicial, estado_final):
    cola = deque()
    cola.append((estado_inicial, []))  # Estado + ruta de movimientos
    visitados = set()
    visitados.add(a_tupla(estado_inicial))

    while cola:
        estado, camino = cola.popleft()

        if estado == estado_final:
            return camino

        x, y = encontrar_vacio(estado)

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nuevo_estado = [fila[:] for fila in estado]
                nuevo_estado[x][y], nuevo_estado[nx][ny] = nuevo_estado[nx][ny], nuevo_estado[x][y]
                if a_tupla(nuevo_estado) not in visitados:
                    visitados.add(a_tupla(nuevo_estado))
                    cola.append((nuevo_estado, camino + [nuevo_estado]))
    return None

# Ejecutar BFS
solucion = bfs(estado_inicial, estado_final)

# Mostrar la solución paso a paso
if solucion:
    print("Solución encontrada en", len(solucion), "movimientos:")
    for paso in solucion:
        for fila in paso:
            print(fila)
        print()
else:
    print("No se encontró solución.")
