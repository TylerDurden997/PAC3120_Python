from PAC3120 import Medidor
import math
import keyboard
import time

def potencia_trifasica_total(potencias_activas,potencias_reactivas,factores_potencias):
    potencia_activa_total = 0
    for potencia_activa in potencias_activas:
        potencia_activa_total += potencia_activa
    potencia_reactiva_total = 0
    for potencia_reactiva in potencias_reactivas:
        potencia_reactiva_total += potencia_reactiva
    factor_potencia_avg = 0
    for factor_potencia in factores_potencias:
        factor_potencia_avg += factor_potencia

    factor_potencia_total = round(factor_potencia_avg/3.0,2)

    potencia_aparente = math.sqrt(pow(potencia_activa_total,2)+pow(potencia_reactiva_total,2))

    potencia_trifasica = potencia_aparente*factor_potencia_total

    return round(potencia_trifasica,2)

def potencia_aparente_trifasica_total(potencias_activas,potencias_reactivas):
    potencia_activa_total = 0
    for potencia_activa in potencias_activas:
        potencia_activa_total += potencia_activa
    potencia_reactiva_total = 0
    for potencia_reactiva in potencias_reactivas:
        potencia_reactiva_total += potencia_reactiva

    potencia_aparente_trifasica_total = math.sqrt(pow(potencia_activa_total,2)+pow(potencia_reactiva_total,2))

    return round(potencia_aparente_trifasica_total,2)

def potencia_aparente_trifasica_total_linea(potencias_activas,potencias_reactivas):

    potencia_aparente_trifasica_total_L1 = math.sqrt(pow(potencias_activas[0],2)+pow(potencias_reactivas[0],2))
    potencia_aparente_trifasica_total_L2 = math.sqrt(pow(potencias_activas[1],2)+pow(potencias_reactivas[1],2))
    potencia_aparente_trifasica_total_L3 = math.sqrt(pow(potencias_activas[2],2)+pow(potencias_reactivas[2],2))

    return [round(potencia_aparente_trifasica_total_L1,2), round(potencia_aparente_trifasica_total_L2,2),round(potencia_aparente_trifasica_total_L3,2)]

def mostrar_valores_medidor(pac_3120, id):
    potencias_activas = pac_3120.get_active_power()
    potencias_reactivas = pac_3120.get_reactive_power()
    factores_potencias = pac_3120.get_power_factor()
    potencia_trifasica = potencia_trifasica_total(potencias_activas,potencias_reactivas,factores_potencias)
    potencia_trifasica_aparente_total = potencia_aparente_trifasica_total(potencias_activas,potencias_reactivas)
    potencia_trifasica_aparente_total_linea = potencia_aparente_trifasica_total_linea(potencias_activas,potencias_reactivas)
    print(f"-------------------------Datos Medidor {id}-------------------------")
    print("Potencia Trifásica: ",potencia_trifasica)
    print("Potencia Trifásica Aparente Total: ",potencia_trifasica_aparente_total)
    print("Potencia Trifásica Aparente Total de Línea: ",potencia_trifasica_aparente_total_linea)

if __name__ == '__main__':
    while True:
        print("---------------Menú Principal---------------")
        print("Por favor elija 1 o 2: ")
        print("1. Cargar tres dispositvos PAC3120")
        print("2. Escriba 2 para salir")
        seleccion = input("Escriba su respuesta: ")
        if seleccion == "2":
            break
        elif seleccion == "1":
            print("Cargue la IP, puerto y Id del equipo a enlazar")
            print("Por ejemplo: 127.0.0.1,502,1")
            print("Recuerde presionar la tecla q para salir del escaneo")
            medidor_1 = input("Ingrese los datos del medidor 1: ")
            medidor_1 = medidor_1.split(",")
            medidor_2 = input("Ingrese los datos del medidor 2: ")
            medidor_2 = medidor_2.split(",")
            medidor_3 = input("Ingrese los datos del medidor 3: ")
            medidor_3 = medidor_3.split(",")
            while True:
                if keyboard.is_pressed("q"):
                    break
                else:
                    pac_3120_1 = Medidor(medidor_1[0],medidor_1[1],int(medidor_1[2]))
                    pac_3120_2 = Medidor(medidor_2[0],medidor_2[1],int(medidor_2[2]))
                    pac_3120_3 = Medidor(medidor_3[0],medidor_3[1],int(medidor_3[2]))
                    mostrar_valores_medidor(pac_3120_1,medidor_1[2])
                    mostrar_valores_medidor(pac_3120_2,medidor_2[2])
                    mostrar_valores_medidor(pac_3120_3,medidor_3[2])
                    time.sleep(1)
        else:
            print("Selección incorrecta, marque alguna de las anteriores")