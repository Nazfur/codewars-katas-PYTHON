def repeats(arr):
    acumulador = 0
    aparecidos = []
    for numero in arr:
        if numero in aparecidos:
            acumulador -= numero
        else:
            acumulador += numero
            aparecidos.append(numero)
        
    return acumulador 
