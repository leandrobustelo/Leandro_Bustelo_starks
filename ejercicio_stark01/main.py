from data_stark import *
from funciones_stark import *
import os



seguir="si"
flag_mayor_m=False
flag_mayor_f=False
flag_menor_m=False
flag_menor_f=False
while(seguir=="si"):
    opcion= mostrar_menu()
    match opcion:
        case 'A':
            lista_aux=buscar_condicon_campo(lista_personajes,"M","genero")
            mostrar_lista_tuplas(lista_aux)            
        case 'B': 
            
            lista_aux=buscar_condicon_campo(lista_personajes,"F","genero")
            mostrar_lista_tuplas(lista_aux)              
        case 'C':
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","M")
            mayor_m=calcular_mayor_lista_dic(lista_aux)
            flag_mayor_m=True 
        case 'D':
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","F")
            mayor_f=calcular_mayor_lista_dic(lista_aux)
            flag_mayor_f=True
        case "E":
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","M")
            menor_m=calcular_menor_lista_dic(lista_aux)
            flag_menor_m=True       
        case "F":
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","F")
            menor_f=calcular_menor_lista_dic(lista_aux)
            flag_menor_f=True      
        case "G":
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","M")
            lista_promediar=capturar_campo(lista_aux,"altura")
            promedio=calcular_promedio_lista(lista_promediar)
            print(f"El prmedio de alturas de genero M --> {promedio}")
        case "H":
            lista_aux=mapear_campo_condicion(lista_personajes,"genero","F")
            lista_promediar=capturar_campo(lista_aux,"altura")
            promedio=calcular_promedio_lista(lista_promediar)
            print(f"El prmedio de alturas de genero F --> {promedio}")
             
        case "I":
            if(flag_mayor_m==True and flag_mayor_f==True and flag_menor_m==True and flag_menor_f==True):
                print(f"El super heroe masculino con mayor altura --> {mayor_m["nombre"]}")
                print()
                print(f"El super heroe femenino con mayor altura --> {mayor_f["nombre"]}")
                print()
                print(f"El super heroe masculino con mayor altura --> {menor_m["nombre"]}")
                print()
                print(f"El super heroe femenino con mayor altura --> {menor_f["nombre"]}")
            else:
                print("Antes de mostrar los nombres debes realizar las operaciones (C a F)")
                
        case "J":
            aux=(cuantos_campo(lista_personajes,"color_ojos"))
            mostrar_dic(aux)
        case 'K':
            aux=(cuantos_campo(lista_personajes,"color_pelo"))
            mostrar_dic(aux)
        case 'L':
            aux=(cuantos_campo(lista_personajes,"inteligencia"))
            mostrar_dic(aux)
        case 'M':
            aux=listar_heroes_campo(lista_personajes,"color_ojos")
            mostrar_dic(aux)
        case 'N':
            aux=listar_heroes_campo(lista_personajes,"color_pelo")
            mostrar_dic(aux)
        case 'O':
            aux=listar_heroes_campo(lista_personajes,"inteligencia")
            mostrar_dic(aux)
        case 'P':
            seguir=Salir_programa()
            
    print()
    os.system("pause")
    os.system('cls')  