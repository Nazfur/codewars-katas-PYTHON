def digitize(n):
    
    n = list(str(n))
    resultado = []
    
    for numero in n[::-1]:
        resultado.append(int(numero))
        
    return resultado
