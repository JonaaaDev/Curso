import random

# entrada
while True:
    n = (input("Introduce tu nombre: ")).upper().strip()
    c = (input("Introduce el nombre: ")).upper().strip()

    # condiciones
    if not n or not c:
        print("Error: Debes escribir ambos nombres.")
        continue

    elif not n.isalpha() or not c.isalpha():
        print("Error: Solo se permiten letras.")
        continue
    break        
# condiciones si todo sale bien
if (n == "JONATHAN" and c == "ANGELINE") or (n == "ANGELINE" and c == "JONATHAN"):
    print("Hay 100% de amor.")

else:
    amor = random.randrange(100)
    print(f"Hay {amor}% de amor.")

"""
Le daría un 7/10.

Motivos:

✅ Funciona correctamente.

✅ Buen manejo de validación de entradas con while True, isalpha() y strip().

✅ Comparaciones claras y lógica correcta.


Mejoras posibles:

Encapsular la lógica en funciones para mayor modularidad.

Usar random.randint(0, 100) para incluir el 100 en el azar.

Añadir comentarios más descriptivos o docstrings.

Manejo más elegante de nombres “especiales” en lugar de comparaciones directas.
"""
