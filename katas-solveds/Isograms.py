def is_isogram(string):
    if string == "": return True
    string = list(string.lower())
    aparecidos = []
    
    for letra in string:
        if letra in aparecidos:
            return False
        else:
            aparecidos.append(letra)
    
    return True

