def multi_table(number):
    numeros = (1,2,3,4,5,6,7,8,9,10)
    resultado = ""
    
    for numero in numeros:
        resultado = resultado + str(numero)+" * "+str(number) + " = " + str(numero*number)
        if numero != 10:
            resultado = resultado + "\n"
        
    return resultado

#sesamo

