#Juan_Neira
def palindromo():
    cadena=""
    validar=True
    while validar:
        try:
            cadena=input("Ingrese la palabra: ")
            break
        except ValueError:
            print("Ingrese una cadena")
    cadena=cadena.replace(" ","").lower()
    izquierda=0
    derecha=len(cadena) -1
    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]:
            validar=False
            break
        izquierda += 1
        derecha -= 1
    if validar:
        return print("Es palindromo")
    else:
        return print("No es palindromo")
palindromo()
