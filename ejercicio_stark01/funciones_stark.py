# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia



def mostrar_menu()->str:
    print("""
                                       CALCULOS DEL SISTEMA.
                                       
            A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
            M. Listar todos los superhéroes agrupados por color de ojos.
            N. Listar todos los superhéroes agrupados por color de pelo.
            O. Listar todos los superhéroes agrupados por tipo de inteligencia
        
            P -->   SALIR DEL PROGRAMA.       
          
          
          
          """)
    opcion=input("Ingrese opciones a realizar: ")
    return opcion.upper()

def buscar_condicon_campo(lista:list,condicion:str,campo:str)->list:
    aux=[]
    for dic in lista:
        if(dic[campo]==condicion):
            aux.append((dic["nombre"],dic["genero"]))
    
    return aux

def mostrar_lista_tuplas(lista:list)->None:
    for dato in lista:
        print(f"""Nombre: {dato[0]}
genero: {dato[1]}""") 
        print()
       
def mapear_campo_condicion(lista:list,campo:str,condicion:str)->list:
    lista_retorno=[]
    for dic in lista:
        if(dic[campo]==condicion):
            lista_retorno.append(dic)
    return lista_retorno

def mostrar_lista_dic(lista:list)->None:

    for dic in lista:
        for clave in dic:
            print(f"{clave} --> {dic[clave]}")
        print()

        
def calcular_mayor_lista_dic(lista:list)->list:
    list_mayor=[]
    aux=lista[0]["altura"]
    
    for dic in lista:
        
        if(dic["altura"]>aux):
            aux=dic["altura"]
            list_mayor.append(dic)
    return list_mayor[-1]

def mostrar_dic(dic:dict)->None:
    for clave in dic:
        print(f"{clave}: {dic[clave]}")
        

def calcular_menor_lista_dic(lista:list)->list:
    list_menor=[]
    aux=lista[0]["altura"]
    
    for dic in lista:
        
        if(dic["altura"]<=aux):
            aux=dic["altura"]
            list_menor.append(dic)
    
    return list_menor[-1]

def  calcular_promedio_lista(lista:list)->float:
    if(isinstance(lista,list)):
        aux=len(lista)
        suma=totalizar_lista(lista)
        if(aux!=0):
            promedio=suma/aux
        else:
            raise ValueError("no esta definido el promedio de una lista vacia.")
        return promedio
    raise  ValueError("lo que ingreso no es una lista.")

def totalizar_lista(lista:list)->int:
    suma=0
    for el in lista:
       suma=suma+el
    return suma

def capturar_campo(lista:list,campo:str)->list:
    lista_retorno=[]
    for dic in lista:
        lista_retorno.append(dic[campo])
    return lista_retorno

def mapear_campo(lista:list,campo:str)->list:
    lista_retorno=[]
    for dic in lista:
        if(dic[campo]==""):
            lista_retorno.append("No tiene")
        else:
            lista_retorno.append(dic[campo])
    return lista_retorno

def buscar_cant_campo_condicion(lista:list,campo:str,condicion:str):
    
    contador=0
    flag=False
    for dic in lista:
        
        if(dic[campo]==condicion or dic[campo]==""):
            contador=contador+1
            flag=True
    if(flag==False):
        raise ValueError("no se encontro ese campo")
    
    return contador

def cuantos_campo(lista:str,campo:str)->dict:
    dic_aux={}
    tipos=list(set(mapear_campo(lista,campo)))
    
    for tipo in tipos:
        
        aux=buscar_cant_campo_condicion(lista,campo,tipo)
        dic_aux[tipo]=aux
    
    return dic_aux

def listar_heroes_campo(lista:list,campo:str)->dict:
    tipos=list(set(mapear_campo(lista,campo)))
    dict_aux={}
    for tipo in tipos:
        
        aux=lista_campo_condicion(lista,campo,tipo)
        dict_aux[tipo]=aux
    return dict_aux
        


def lista_campo_condicion(lista:list,campo:str,condicion:str)->list:
    lista_return=[]
    flag=False
    for dic in lista:
        if(dic[campo]==condicion or dic[campo]==""):
            lista_return.append(dic["nombre"])
            flag=True
    if(flag==False):
        raise ValueError("no se encontro ese campo")
    return lista_return



def Salir_programa()->str:
    while(True):
        print()
        rta=input('Desea salir del programa? ')
        if(rta=="si"):
            seguir="no"
            return seguir
            
        elif(rta=='no'):
            seguir="si"
            return seguir
        else:
            
            print("Error. conteste con 'si' o 'no' ")
            