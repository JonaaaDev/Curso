try:
    year = int(input("Cuántos años tienes: "))
    if year > 0:
        meses = year * 12
        print(f"Tienes {meses} meses")
    else:
        print("ERROR.  Numero negativo.")    
except ValueError as e:
    print({e})      

"""
Para tu ejercicio y código actual, yo le daría un 9/10. ✅

Por qué:

Funciona correctamente para enteros positivos.

Maneja errores con try/except.


Por mejorar:

El print({e}) no es lo ideal, mejor print(e).

No acepta decimales, solo enteros.

Podrías agregar un cálculo de días o mostrar un mensaje más divertido para aprender más.
"""
