import os
os.system("cls")
import random

print ("   Welcome to AutoSeguro")
print ("Completa los datos en el Menu")
print ("            De")
print("          Abajo! :D")

#Nota: se que se puede hacer de otra forma pero yo lo queria hacerlo así :D

vehiculos = []

def agregar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo (Automóvil, Camión, Camioneta, Moto): ")
    patente = input("Ingrese la patente: ")
    marca = input("Ingrese la marca del vehículo: ")
    precio = int(input("Ingrese el precio del vehículo (mayor a $5.000.000): "))
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    multas = input("Ingrese las multas (separadas por coma, o 0 si no hay): ").split(',')
    run_dueno = input("Ingrese el RUN del dueño: ")
    nombre_dueno = input("Ingrese el nombre del dueño: ")
    
    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "fecha_registro": fecha_registro,
        "multas": multas,
        "run_dueno": run_dueno,
        "nombre_dueno": nombre_dueno
    }
    vehiculos.append(vehiculo)
    print("Vehículo agregado exitosamente!")
    
    
    
def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            print("Información del vehículo:")
            for key, value in vehiculo.items():
                print(f"{key.capitalize()}: {value}")
            return
    print("Vehículo no encontrado.")
    
    
    
def imprimir_certificados():
    patente = input("Ingrese la patente del vehículo para imprimir certificados: ")
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            certificado = {
                "emision_contaminantes": random.randint(1500, 3500),
                "anotaciones_vigentes": random.randint(1500, 3500),
                "multas": random.randint(0,0)
            }
            print(f"Certificado de Emisión de contaminantes: {certificado['emision_contaminantes']}")
            print(f"Certificado de Anotaciones vigentes: {certificado['anotaciones_vigentes']}")
            print(f"Certificado de Multas: {certificado['multas']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Nombre del dueño: {vehiculo['nombre_dueno']}")
            print(f"RUN del dueño: {vehiculo['run_dueno']}")
            return
    print("Vehículo no encontrado.")



def menu():
    while True:
        print("(=========================)")
        print("\t**MENU**")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir")
        print("(=========================)")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_vehiculo()
            
        elif opcion == "2":
            buscar_vehiculo()
            
        elif opcion == "3":
            imprimir_certificados()
            
        elif opcion == "4":
            print("Volvere... (dijo el terminator)")
            break
        else:
            print("Opción inválida")
            
menu()