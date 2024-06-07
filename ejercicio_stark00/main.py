from funcionesstark00 import *
from data00 import *
import os



seguir= "si"
flag_mayor=False
flag_menor=False
while(seguir=="si"):
    
    opcion=menu_principal()
    print()
    
    match opcion:
        
        case "A":
            analizar_datos(lista_personajes)
        case "B":
            mostrar_nombres_heroes(lista_personajes,"nombre")
        case "C":
            mostrar_nombres_alturas_heroes(lista_personajes,"nombre","altura")
        case "D":
            aux_mayor=calcular_mayor_heroe(lista_personajes,"altura")
            flag_mayor=True  
            print("Calculo realizado")
        case "E":
            aux_menor=calcular_menor_heroe(lista_personajes,"altura")
            flag_menor=True
            print("Calculo realizado")  
        case "F":
            aux=mapear_campo(lista_personajes,"altura")
            promedio=calcular_promedio_lista(aux)
            print(f"El promedio total de las alturas de los heroes es --> {promedio}")
        case "G":
            if(flag_mayor==True and flag_menor==True):
                print("Persona mayor")
                mostrar_dic(aux_mayor)
                print()
                print("Persona menor")
                mostrar_dic(aux_menor)
            else:
                print("Primero calcula el mayor y el menor.")  
        case "H":
            aux_mayor_peso=calcular_mayor_heroe(lista_personajes,"peso")
            mostrar_dic(aux_mayor_peso)
            print()
            aux_menor_peso=calcular_menor_heroe(lista_personajes,"peso")
            mostrar_dic(aux_menor_peso)    
        case "I":
            seguir=Salir_programa()
    print()
    os.system("pause")
    os.system("cls")