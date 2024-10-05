#Escribe una función en Python que determine si un número es perfecto.
#Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el número mismo). 
#Por ejemplo, el número 6 es perfecto porque sus divisores (1, 2 y 3) suman 6. Escribe una función que reciba un número 
#entero positivo y devuelva un mensaje indicando si el número es perfecto o no. Tu implementación debe recorrer todos los posibles 
#divisores menores al número dado, calcular su suma y luego verificar si esta suma es igual al número original.

def es_numero_perfecto(numero):
    
    suma_divisores = 0
    
    for i in range (1,numero):
        if numero % i == 0:
            suma_divisores +=i
    
    if suma_divisores == numero:
        return f"{numero} es un número perfecto."
    else:
        return f"{numero} no es un número perfecto."

#pedir al usuario que ingrese el número

while True:
    
    try:
        
        numero_usuario = int(input("Por favor ingrese, un número entero postivo, \npara verificar si es si es perfecto: "))
        if numero_usuario > 0:
            break
        else:
            print("El número debe ser mayor a 0")
            
    except ValueError:
        print("Entrada inválidad. Por favor ingrese un número entero postivo mayor a 0")

resultado = es_numero_perfecto(numero_usuario)
print(resultado)
