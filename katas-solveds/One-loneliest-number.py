def loneliest(number): 
    es_minimo = False
    number = list(str(number))
    temp = []
    indice = 0
    for i in number:
        temp.append(int(i))
    
    number = temp
    temp = []
    check = []
    
    
    for numero in number:
        
        if numero == 1:
            check.append(indice)
        
        temp.append(sum(number[indice+1:indice+numero+1:1])+sum(number[:indice][::-1][:numero]))
        indice += 1
        

        
        
    for i in check:
        if min(temp) == temp[i]:
            return True
    return False
