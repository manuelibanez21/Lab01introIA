from collections import deque

tamaño = 3
inicio = (0, 0)
meta = (tamaño-1, tamaño-1)
obstaculos = {(1, 1)}

acciones = {
    "derecha": (0, 1),
    "izquierda": (0, -1),
    "abajo": (1, 0),
    "arriba": (-1, 0)
}

def mover(estado, accion, obstaculos=set()):
    if accion not in acciones:
        return estado
    dx, dy = acciones[accion]
    nuevo_estado = (estado[0] + dx, estado[1] + dy)
    if not (0 <= nuevo_estado[0] < tamaño and 0 <= nuevo_estado[1] < tamaño):
        return estado
    if nuevo_estado in obstaculos:
        return estado
    return nuevo_estado

def buscar_camino(inicio, meta, obstaculos):
    cola = deque([(inicio, [inicio])])
    visitados = set([inicio])
    while cola:
        estado, camino = cola.popleft()
        if estado == meta:
            return camino
        for accion in acciones:
            nuevo_estado = mover(estado, accion, obstaculos)
            if nuevo_estado not in visitados and nuevo_estado != estado:
                visitados.add(nuevo_estado)
                cola.append((nuevo_estado, camino + [nuevo_estado]))
    return None

print("=== LABERINTO MANUAL ===")
print(f"Inicio: {inicio}, Meta: {meta}, Obstáculos: {obstaculos}")
print("Movimientos posibles:", list(acciones.keys()))

estado = inicio
camino_manual = [estado]

while estado != meta:
    accion = input("Ingresa movimiento (o 'salir' para parar manual): ").strip().lower()
    if accion == "salir":
        break
    estado_nuevo = mover(estado, accion, obstaculos)
    if estado_nuevo == estado:
        print("Movimiento inválido o bloqueado 🚫")
    else:
        estado = estado_nuevo
        camino_manual.append(estado)
        print("Estado actual:", estado)

if estado == meta:
    print("\n¡Meta alcanzada manualmente! ✅")
    print("Camino recorrido:", camino_manual)
else:
    print("\nNo se llegó manualmente, ejecutando búsqueda automática 🔎...")
    camino_auto = buscar_camino(inicio, meta, obstaculos)
    if camino_auto:
        print("Camino encontrado automáticamente:", camino_auto)
    else:
        print("No existe camino disponible 🚫")
