#Melisa Castillon 
def suma_digitos():
    while True:
        try:
            numero=int(input("Ingrese el numero: " ))
            if numero<0:
                print("Ingrese un numero positivo")
            else:
                break
        except ValueError:
            print("Ingrese un numero entero")
    str_numero=str(numero)
    while len(str_numero)>1:
        suma=0
        for i in str_numero:
            suma+=int(i)
        str_numero=str(suma)
    return int(str_numero)
resultado=suma_digitos()
print("El resultado de la suma de dígitos es:", resultado)