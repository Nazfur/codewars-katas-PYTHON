def is_isogram(word: str) -> bool:
    if word == "": return False
    
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    aparecido = 0
    apariciones = 0
    word = list(word.lower())
    
    for letra in word:
        if letra in abecedario:
            apariciones = 1
            break
    print(apariciones)
    if apariciones != 1:
        return False
    
    apariciones = 0

    for letra in word:
        aparecido = 0
        if letra in abecedario:
            if apariciones == 0:
                for letra_comparada in word:
                    if letra_comparada == letra:
                        apariciones += 1
            for letra_comparada in word:
                if letra_comparada == letra:
                    aparecido += 1
            if aparecido != apariciones:
                return False
    
    
    return True
