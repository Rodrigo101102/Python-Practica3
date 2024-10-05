listaNumero=[]
def ingresarNumero():
    while(True):
        try:
            cantidadNumero=int(input("Indique la cantidad de numero que va usar en la lista: "))
            if cantidadNumero>0:
                for i in range(cantidadNumero):
                    numero=float(input(f"Ingrese el número: {i+1}: "))
                    listaNumero.append(numero)
                break
            else:
                print("Ingrese un numero positivo")
        except ValueError:
            print("Ingrese un numero entero")
def calcular():
    if len(listaNumero) == 0: 
        print("La lista está vacía. No se puede calcular.")
        return
    sumaNumero=0    
    for numero in listaNumero:
        sumaNumero+=numero
    promedio=round(sumaNumero/(len(listaNumero)),2)
    lista_ordenada=sorted(listaNumero)
    medio=len(listaNumero)//2
    if len(listaNumero)%2==0:
        numero1=lista_ordenada[medio-1]
        numero2=lista_ordenada[medio]
        media=(numero1+numero2)/2
    else:
        media=lista_ordenada[medio]
          # Calcular la moda usando solo bucles
    frecuencias = {}
    
    # Contar frecuencias
    for num in listaNumero:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1

    max_frecuencia = 0
    for v in frecuencias.values():
        if v > max_frecuencia:
            max_frecuencia = v

    modas = []
    for k in frecuencias:  # Agregar las modas a la lista
        if frecuencias[k] == max_frecuencia:
            modas.append(k)

    return media, promedio, modas

ingresarNumero()
resultado = calcular()

if resultado:
    media, promedio, modas = resultado
    print("Media:", media)
    print("Promedio:", promedio)
    print("Moda:", modas)
