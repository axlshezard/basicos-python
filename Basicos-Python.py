# Estructura de control: Condicional (if, elif, else)
def condicional_ejemplo(x):
    if x > 0:
        print(f"{x} es positivo")
    elif x < 0:
        print(f"{x} es negativo")
    else:
        print(f"{x} es cero")

# Estructura de control: Bucle for
def bucle_for_ejemplo(lista):
    for elemento in lista:
        print(f"Elemento: {elemento}")

# Estructura de control: Bucle while
def bucle_while_ejemplo(n):
    while n > 0:
        print(f"Cuenta regresiva: {n}")
        n -= 1

# Estructura de control: Break
def bucle_con_break():
    for i in range(10):
        if i == 5:
            print("Se alcanzó el número 5, saliendo del bucle")
            break
        print(i)

# Estructura de control: Continue
def bucle_con_continue():
    for i in range(10):
        if i % 2 == 0:
            continue
        print(f"Número impar: {i}")

# Estructura de control: Try-Except (manejo de excepciones)
def manejo_excepciones(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    else:
        print(f"El resultado de {a} dividido por {b} es {resultado}")

# Ejercicio 1: Operaciones básicas y variables
def operaciones_basicas():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b}")

def intercambiar_valores():
    x = input("Ingresa el valor de x: ")
    y = input("Ingresa el valor de y: ")
    x, y = y, x
    print(f"Valores intercambiados: x = {x}, y = {y}")

# Ejercicio 2: Estructuras de datos
def manipular_lista():
    lista = []
    lista.append(1)
    lista.append(2)
    lista.append(3)
    print(f"Lista: {lista}")
    lista.remove(2)
    print(f"Lista después de remover 2: {lista}")
    print(f"Primer elemento: {lista[0]}")

def manipular_diccionario():
    diccionario = {"nombre": "Juan", "edad": 25}
    diccionario["ciudad"] = "Ciudad de México"
    print(f"Diccionario: {diccionario}")
    print(f"Valor para 'nombre': {diccionario['nombre']}")

# Ejercicio 3: Bucles
def numeros_pares():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

def suma_n_numeros(n):
    suma = 0
    while n > 0:
        suma += n
        n -= 1
    print(f"Suma de los primeros n números: {suma}")

# Ejercicio 4: Funciones
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio 5: Manipulación de cadenas
def invertir_cadena(cadena):
    return cadena[::-1]

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

# Ejercicio 6: Manejo de archivos
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        for linea in file:
            print(linea.strip())

def escribir_archivo(archivo, nombres):
    with open(archivo, 'w') as file:
        for nombre in nombres:
            file.write(f"{nombre}\n")

# Ejercicio 7: Listas y comprensión de listas
def cuadrados_numeros():
    cuadrados = [x**2 for x in range(1, 11)]
    print(f"Cuadrados de 1 a 10: {cuadrados}")

def filtrar_pares(lista):
    pares = [x for x in lista if x % 2 == 0]
    print(f"Números pares: {pares}")

# Ejercicio 8: Manejo de excepciones
def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        print("Error: no es un número válido")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            print(f"Número ingresado: {numero}")
            break
        except ValueError:
            print("Error: Debes ingresar un número")

# Ejercicio 9: Programación orientada a objetos
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Ejercicio 10: Módulos y paquetes
import math

def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# Ejecución de ejemplos
if __name__ == "__main__":
    print("Condicional:")
    condicional_ejemplo(5)
    condicional_ejemplo(-3)
    condicional_ejemplo(0)

    print("\nBucle for:")
    bucle_for_ejemplo([1, 2, 3, 4, 5])

    print("\nBucle while:")
    bucle_while_ejemplo(5)

    print("\nBucle con break:")
    bucle_con_break()

    print("\nBucle con continue:")
    bucle_con_continue()

    print("\nManejo de excepciones:")
    manejo_excepciones(10, 2)
    manejo_excepciones(10, 0)

    operaciones_basicas()
    intercambiar_valores()

    manipular_lista()
    manipular_diccionario()

    numeros_pares()
    suma_n_numeros(10)

    print(f"Factorial de 5: {factorial(5)}")
    print(f"¿7 es primo? {es_primo(7)}")

    cadena = "Hola Mundo"
    print(f"Invertir cadena: {invertir_cadena(cadena)}")
    print(f"Número de vocales en '{cadena}': {contar_vocales(cadena)}")

    escribir_archivo('nombres.txt', ['Juan', 'Carlos', 'Ana'])
    leer_archivo('nombres.txt')

    cuadrados_numeros()
    filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    convertir_a_entero("123")
    pedir_numero()

    c = Circulo(5)
    print(f"Área del círculo: {c.area()}")

    p = Persona("Juan", 25)
    p.saludo()

    print(f"Hipotenusa de un triángulo con lados 3 y 4: {calcular_hipotenusa(3, 4)}")
