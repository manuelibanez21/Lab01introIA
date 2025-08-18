# SEGUNDO PUNTO LABORATORIO

# Problema 1: Mascota triste

# Defino estados y acciones, y el objetivo final
estados = ["triste", "contenta"]
acciones = ["Dar comida", "Nada"]

Estado = "triste"
meta = "contenta"

# Muestra estado inicial de la mascota

print("Estado de la mascota:", Estado)

# Ciclo para monitorear hasta alcanzar el estado objetivo

while Estado != meta:
    accion = "Dar comida" 
    print("accion realizada:", accion)

    if accion == "Dar comida" :
            Estado = "contenta"
    else:
        Estado = "triste"

print("Estado actual:" , Estado)

#---------------------------------------------------------------------------------------------------------------

# Problema 2: tesoro del pirata

# Defino acciones, es decir los movimientos del pirata

Acciones2 = { "Arriba":(0,1),
             "Abajo":(0,-1),
             "Izquierda":(-1,0),
             "Derecha":(1,0)}

# Estados iniciales y meta

Estado2 = (0,0)
Meta2 = (2,2)

print("posición actual del pirata:", Estado2)
camino = [Estado2]

# Algoritmo para llegar al tesoro, similar al bucle anterior

while Estado2 != Meta2:
     x2, y2 = Estado2
     
     if x2 < Meta2[0]:
          accion2 = "Derecha"
     elif y2 < Meta2[1]:
          accion2 = "Arriba"
     else:
        accion2 = None
    
     if accion2:
      dx, dy = Acciones2[accion2]
      Estado2 = (x2 + dx, y2 + dy)
      camino.append(Estado2)
      print(f"Acción: {accion2} → Nueva posición: {Estado2}") 

print("tesoro encontrado!")
print("camino:", camino)

