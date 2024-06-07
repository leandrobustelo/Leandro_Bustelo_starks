def menu_principal()->str:
    print("""
                                CALCULOS DEL SISTEMA.
            A. Analizar detenidamente el set de datos
            B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
            C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
            D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
            E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
            F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
            G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
            H. Calcular e informar cual es el superhéroe más y menos pesad
            
            I. salir del programa
            
                    
          """)
    opcion=input("Ingrese opciones a realizar: ")
    return opcion.upper()

def mostrar_dic(dic:dict)->None:
    """
    Imprime los elementos de un diccionario.

    Args:
    - dic (dict): El diccionario que se imprimirá.

    Returns:
    - None: Esta función no devuelve ningún valor, solo imprime los elementos del diccionario.
    """
    for clave in dic:
        print(f"{clave}: {dic[clave]}")

def mapear_campo(lista:list,campo:str)->list:
    """
    Mapea un campo específico en una lista de diccionarios y devuelve una lista con los valores correspondientes.

    Args:
    - lista (list): La lista de diccionarios en la que se buscará el campo.
    - campo (str): El nombre del campo que se mapeará.

    Returns:
    - list: Una lista con los valores del campo especificado en la lista de diccionarios.
    """
    lista_retorno=[]
    for dic in lista:
        if(dic[campo]==""):
            lista_retorno.append("No tiene")
        else:
            lista_retorno.append(dic[campo])
    return lista_retorno

def totalizar_lista(lista:list)->int:
    """
    Calcula la suma de los elementos de una lista de números.

    Args:
    - lista (list): La lista de números que se sumarán.

    Returns:
    - int: La suma de los elementos de la lista.
    """
    suma=0
    for el in lista:
       suma=suma+el
    return suma
 
def  calcular_promedio_lista(lista:list)->float:
    """
    Calcula el promedio de los elementos de una lista de números.

    Args:
    - lista (list): La lista de números de la que se calculará el promedio.

    Returns:
    - float: El promedio de los elementos de la lista.

    Raises:
    - ValueError: Si la lista está vacía.
    - ValueError: Si el argumento pasado no es una lista.
    """
    if(isinstance(lista,list)):
        aux=len(lista)
        suma=totalizar_lista(lista)
        if(aux!=0):
            promedio=suma/aux
        else:
            raise ValueError("no esta definido el promedio de una lista vacia.")
        return promedio
    raise  ValueError("lo que ingreso no es una lista.")
def analizar_datos(lista:list)->None:
    
    for dic in lista:
        for clave in dic:
            print(f"{clave} --> {dic[clave]}")
        print("---------------------------------")
        
def mostrar_nombres_heroes(lista:list,campo:str):
    for dic in lista:
        print(f"Nombre: {dic[campo]}")
        print()
        
def mostrar_nombres_alturas_heroes(lista:list,campo1:str,campo2:str):
    for dic in lista:
        print(f"Nombre: {dic[campo1]}")
        print(f"Altura: {dic[campo2]}")
        print()

       
def calcular_mayor_heroe(lista:list,campo:list)->int:
    if(isinstance(lista,list)):
        if(len(lista)!=0):
            
            lista_mayor=[]
            mayor=lista[0][campo]
            for dic in lista:
                if(dic[campo]>mayor):
                    mayor=dic[campo]
                    lista_mayor.append(dic)
            return lista_mayor[-1]
        
        else:
            raise ValueError("No se puede calcular el mayor en una lista vacia.")
    raise ValueError("Lo que ingreso no es una lista.")



def calcular_menor_heroe(lista:list,campo)->int:
    if(isinstance(lista,list)):
        if(len(lista)!=0):
            
            lista_menor=[]
            mayor=lista[0][campo]
            for dic in lista:
                if(dic[campo]<=mayor):
                    mayor=dic[campo]
                    lista_menor.append(dic)
            return lista_menor[-1]
        
        else:
            raise ValueError("No se puede calcular el mayor en una lista vacia.")
    raise ValueError("Lo que ingreso no es una lista.")

def Salir_programa()->str:
    """
    Solicita al usuario que confirme si desea salir del programa.

    Returns:
    - str: "no" si el usuario elige no salir del programa, "si" si el usuario elige salir del programa.

    Note:
    - Esta función solicita al usuario que ingrese "si" o "no" para confirmar si desea salir del programa. Devuelve "si" si el usuario elige salir y "no" si elige no salir.
    """

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
