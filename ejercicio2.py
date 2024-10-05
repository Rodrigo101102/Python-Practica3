#Desarrolla una función en Python que invierta una cadena de texto sin utilizar el operador de slicing.

def invertir_cadena(cadena):
    
    cadena_invertida = ""
    
    
    for char in cadena:
        
        cadena_invertida = char + cadena_invertida
    
    return cadena_invertida


def es_texto_valido(texto):
    return texto.isalpha()  


while True:
    texto_usuario = input("Introduce una cadena de texto (sin números): ")
    
    if es_texto_valido(texto_usuario):
        break 
    else:
        print("Error: Por favor, introduce solo texto, sin números.")


print("Cadena invertida:", invertir_cadena(texto_usuario))
