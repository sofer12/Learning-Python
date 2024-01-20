# tipos de datos en Python
#Python es un lenguaje dinámicamente tipado no es obligatorio asignar el tipo de dato a una variable 
#Python es un lenguaje e INTERPRETADO

#1. Numéricos
## ENTEROS Z => int
num1 = 42
print("Num1: ", type(num1))
##Flotantes o decimales (reales) => float
num2 = 50.5
print("Num2: ", type(num2))
## Clomplejos=> complex
num3 = 3j
print("Num3: ", type(num3))

#2. Cadena
my_name = "Sofia"
print("my_name", type(my_name))
my_lastname = "Guarin"
print("my_lastname", type(my_lastname))
profile = '''jhasgdkashgcfsajf
ashdgjshgd
jgsdfhsdg'''
print("profile", type(profile))
address = "Monterrey"
print("address", type(address))

a = 1
b = 2
suma1 = a + b #suma aritmetica

c = "1"
d = "1"
suma2 = c + d #suma de cadenas (Concatenación)

print("suma1 :", suma1) #2
print("suma2 :", suma2) #


#3. Lógicos (Valores o expresiones booleanas)
usuario_activo = True
print ("usuario_activo", type(usuario_activo))

pago_realizado = True
print ("pago_realizado", type (pago_realizado))

#4. Listas
frutas = ['Apple', 'Banana']
Color = ['Blue', 'Red', 'White', 'Green', 'Brown']
detodito = ['Sofia', '24', '1999', 'Monte', 170.8, 24]

print(frutas)
print ("frutas", type(frutas))
print(Color)
print ("color", type(Color))
print (detodito)
print ("detodito", type(detodito [4]))

#5. Tuplas
#6. Diccionarios
#7. Conjuntos