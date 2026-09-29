def duplicate_encode(word):
    
    resultado  = ""
    duplicados = []
    palabra = word.lower()
    word = list(word.lower())
    palabra = list(palabra)
    
    
    for caracter in word:
        if caracter not in duplicados:
            palabra.remove(caracter)
            if caracter in palabra:
                duplicados.append(caracter)
        
        if caracter in duplicados:
            resultado += ")"
        else:
            resultado += "("
        
        print(caracter)
    
    return resultado
