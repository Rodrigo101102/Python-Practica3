def calcular_factorial():
    while True:
        try:
            numero=int(input("Ingrese un numero : "))
            if numero>=0:
                break
            else:
                print("Ingrese un numero positivo")
        except ValueError:
            print("Error, ingrese un numero entero")
    original_numero = numero
    if numero==0 or numero==1:
        print(f"El factorial de {numero} es 1")
    else:
        acumulador=1
        while numero>1:
            acumulador=acumulador*(numero)
            numero-=1
        print(f"El factorial de {original_numero} es {acumulador}")
    
calcular_factorial()    