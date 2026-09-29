def get_count(sentence):
    vocales = ['a','e','i','o','u']
    resultado = 0
    
    for letra in vocales:
        resultado += sentence.count(letra)
    
    return resultado

