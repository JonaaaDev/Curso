import time

la_lista = []

def help():
    print("escribe salir en título para salir de la app")

print("Bienvenido al programa\n")

while True:
    titulo = input("Titulo: ").upper()
    
    if titulo == "SALIR":
        break
    elif titulo == "HELP":
        help()
    
    desc = input("Descripción: ")
    
    prioridad = input("Prioridad de la tarea: ").upper()
    
    if prioridad == "BAJO" or prioridad == "MEDIO" or prioridad == "ALTA":
        dic = {
            "Título": titulo,
            "Desc": desc,
            "Prioridad": prioridad
        }
        la_lista.append(dic)
        print("\nLista de tareas:")
        for i, tarea in enumerate(la_lista, 1):
            print(f"{i}. {tarea['Título']} - {tarea['Desc']} - {tarea['Prioridad']}")
        time.sleep(3)
    else:
        print("Error tienes que indicar la prioridad con bajo, medio, alto")


"""
🔹 Puntos fuertes:

Valida correctamente la prioridad.

Lista las tareas de forma legible.

Incluye comandos útiles (SALIR y HELP).

Uso de diccionarios y listas correctamente.


🔹 Puntos a mejorar:

1. Persistencia: guardar las tareas en un archivo (JSON) para no perderlas al cerrar.


2. Opciones extra: marcar como completadas, eliminar tareas, ver solo las pendientes.


3. Validación adicional: evitar títulos o descripciones vacías.


4. Podría tener un menú más estructurado en lugar de solo pedir título, descripción y prioridad cada vez.
"""
