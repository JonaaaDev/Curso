import random

print("*****MI CALCULADORA*****\n")

usuario = input("Escribe el primer nombre: ").strip().capitalize()

if not usuario.isalpha():
    print("Escribe nombres reales.\n")
    exit()

if len(usuario) > 10:
    print("Muy largo.")
    exit()
elif len(usuario) < 3:
    print("Muy corto.")
    exit()        

inv = input("Escribe el segundo nombre: ").strip().capitalize()

if not inv.isalpha():
    print("Escribe nombres reales.\n")
    exit()

if len(inv) > 10:
    print("Muy largo.")
    exit()
elif len(inv) < 3:
    print("Muy corto.")
    exit()  

if inv == usuario:
    print("Son los mismos nombres.")
    exit()

if (inv == "Jonathan" or inv == "Angeline") and (usuario == "Jonathan" or usuario == "Angeline"):
    num = 100
    print(f"El amor entre {usuario} y {inv} es: {num}%!")
else:
    num = random.randint(0,100)
    print(f"El amor entre {usuario} y {inv} es: {num}%!")
    
    if num == 100:
        print("Aquí hay muchísimo amor. Deben de ser novios.")
    elif num >= 90:
        print("Hay bastante amor, Deben de probar.")
    elif num >= 80:
        print("Aquí puede haber algo serio.")
    elif num >= 70:
        print("Hay algo de cariño, pero todavía no es seguro.")
    elif num >= 50:
        print("Amistad con posibilidades, pero el amor es leve.")
    elif num >= 30:
        print("No hay mucho amor, mejor como amigos.")
    else:
        print("Casi no hay amor, es mejor no ilusionarse.")
