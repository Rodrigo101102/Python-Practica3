#Melisa Castillon 
class Usuario:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso 
        self.altura = altura  
        self.actividad_fisica = []
        self.alimentacion = []
        self.total_agua_bebida = 0
        self.imc_calculado = True 

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)

    def recomendar_agua(self):
        agua_recomendada = self.peso * 35  
        return round(agua_recomendada / 1000, 2)  

    def recomendar_calorias(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return 2500 
        elif 18.5 <= imc < 24.9:
            return 2000  
        else:
            return 1500 

    def beber_agua(self, litros):
        self.total_agua_bebida += litros

    def registrar_actividad(self, actividad, duracion):
        self.actividad_fisica.append({'actividad': actividad, 'duracion': duracion})

    def registrar_alimentacion(self, comida, calorias):
        self.alimentacion.append({'comida': comida, 'calorias': calorias})

    def total_calorias_consumidas(self):
        return sum(item['calorias'] for item in self.alimentacion)

    def mostrar_resumen(self):
        print(f"\nResumen de {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")

        if self.imc_calculado:
            imc = self.calcular_imc()
            print(f"IMC: {imc} - Estado: {self.estado_salud(imc)}")
        else:
            print("IMC no calculado aún.")

        print(f"Total de agua bebida: {self.total_agua_bebida} litros")
        print(f"Calorías consumidas hoy: {self.total_calorias_consumidas()}")
        print(f"Calorías recomendadas: {self.recomendar_calorias()}")

        print("\nActividades físicas realizadas:")
        for actividad in self.actividad_fisica:
            print(f"- {actividad['actividad']}: {actividad['duracion']} minutos")

        print("\nComidas registradas:")
        for comida in self.alimentacion:
            print(f"- {comida['comida']}: {comida['calorias']} calorías")

        self.conclusion()

    def estado_salud(self, imc):
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"

    def conclusion(self):
        agua_recomendada = self.recomendar_agua()
        calorias_recomendadas = self.recomendar_calorias()

        if self.total_agua_bebida < agua_recomendada:
            print("\n¡Cuidado! No has alcanzado la cantidad recomendada de agua. \nRecuerda, la hidratación es clave para un cuerpo saludable. ¡Bebe más agua!")
        else:
            print("\n¡Excelente trabajo! Has cumplido con tu meta de hidratación.\n¡Sigue así y mantén tu energía al máximo!")

        if self.total_calorias_consumidas() < calorias_recomendadas:
            print("Asegúrate de no quedarte corto en tus calorías diarias.\nTu cuerpo necesita energía para funcionar correctamente.")
        else:
            print("¡Bien hecho! Estás consumiendo suficientes calorías para mantener tu energía.")


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def main():
    print("¡Bienvenido al Sistema de Gestión de Bienestar Físico!")
    
    nombre = input("Ingrese su nombre: ")
    
    edad = int(pedir_numero("Ingrese su edad: "))
    peso = pedir_numero("Ingrese su peso en kg: ")
    altura = pedir_numero("Ingrese su altura en metros: ")

    usuario = Usuario(nombre, edad, peso, altura)

    while True:
        print("\n--- Menú ---")
        print("1. Recomendaciones de agua y calorías diarias")
        print("2. Registrar agua bebida")
        print("3. Registrar actividad física")
        print("4. Registrar alimentación")
        print("5. Mostrar resumen de rutina")
        print("6. Calcular y reiniciar IMC")
        print("7. Mostrar perfil")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                agua_recomendada = usuario.recomendar_agua()
                calorias_recomendadas = usuario.recomendar_calorias()
                print(f"Debes beber aproximadamente {agua_recomendada} litros de agua al día.")
                print(f"Debes consumir aproximadamente {calorias_recomendadas} calorías al día.")

            elif opcion == "2":
                litros = pedir_numero("¿Cuántos litros de agua has bebido?: ")
                usuario.beber_agua(litros)
                print(f"Total de agua bebida hoy: {usuario.total_agua_bebida} litros.")

            elif opcion == "3":
                actividad = input("Describe la actividad física: ")
                duracion = int(pedir_numero("Duración en minutos: "))
                usuario.registrar_actividad(actividad, duracion)
                print("Actividad registrada exitosamente.")

            elif opcion == "4":
                comida = input("Ingresa la comida consumida: ")
                calorias = int(pedir_numero("Cantidad de calorías: "))
                usuario.registrar_alimentacion(comida, calorias)
                print("Comida registrada exitosamente.")

            elif opcion == "5":
                usuario.mostrar_resumen()

            elif opcion == "6":
                print("Reiniciando el cálculo de IMC...")
                usuario.peso = pedir_numero("Ingrese su nuevo peso en kg: ")
                usuario.altura = pedir_numero("Ingrese su nueva altura en metros: ")
                usuario.imc_calculado = True
                print("Nuevos datos ingresados. IMC recalculado.")

            elif opcion == "7":
                imc = usuario.calcular_imc()
                estado = usuario.estado_salud(imc)
                print(f"\nPerfil de {usuario.nombre}:")
                print(f"IMC: {imc} - Estado: {estado}")
                print(f"Peso: {usuario.peso} kg")
                print(f"Altura: {usuario.altura} m")
                print(f"Edad: {usuario.edad}")

            elif opcion == "8":
                print("Saliendo del sistema. ¡Cuida tu salud!")
                break

            else:
                print("Opción no válida, por favor elige otra.")

        except ValueError:
            print("Error en la entrada de datos. Asegúrese de ingresar valores válidos.")

# Ejecutar el sistema
main()
