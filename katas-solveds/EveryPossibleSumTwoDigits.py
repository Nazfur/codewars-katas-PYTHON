def digits(n):
    
    resultado_final = []
    indice = 0
    
    n = list(str(n)) 
    '''
    n es un numero entero como 123, y para que podamos trabajar comodos
    transformo n en un string, para luego poder transformarlo en una lista
    '''
    
    # Todas las variables necesarias para el programa 
    
    while indice < len(n):
        for numero in n[indice+1:]:
            resultado_final.append(int(n[indice]) + int(numero))
        
        indice = indice + 1
    
    '''El bucle while se encarga de repetirse segun la longitud de la lista, 
    el contador es la variable indice que es la misma que vamos a reutilizar en la
    lista n para hacer la suma, el bucle for va a recorrer la lista tomando sus valores
    para sumarlo con n[indice], para evitar que se repita la suma, como [1,2,3] -> 1+1.a.. o 2+1...
    le decimos que empieze a recorrer la lista desde el indice + 1 hasta el final ':'.
    Cuando hagamos la suma, tenemos que recordar que se esta sumando 2 caracteres, por eso forzamos el tipo a int()
    '''
    
    return resultado_final # Devolvemos el resultado final
