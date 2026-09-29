def two_oldest_ages(ages):
    resultado = [0,0] # No funciona con edades negativas, aunque no tiene sentido
    
    for edad_vieja in ages:
        if edad_vieja > resultado[1]:
            resultado[0] = resultado[1]
            resultado[1] = edad_vieja
        elif edad_vieja > resultado[0]:
            resultado[0] = edad_vieja
    
    return resultado

