def rot13(message):
    
    letra_encriptada = ''
    es_mayuscula = False
    resultado = ""
    ascii = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    
    message = list(message)
    
    # Creacion y transformación de variables necesarias
    
    for letra in message:
        
        if letra.lower() in ascii:
            if letra.isupper() == True:
                es_mayuscula = True
            else:
                es_mayuscula = False

            letra_encriptada = ascii[(ascii.index(letra.lower())+13)%26]

            if es_mayuscula:
                letra_encriptada = letra_encriptada.upper()
            else:
                letra_encriptada = letra_encriptada.lower()

            resultado = resultado + letra_encriptada
        
        else:
            resultado = resultado + letra
    
    return resultado

