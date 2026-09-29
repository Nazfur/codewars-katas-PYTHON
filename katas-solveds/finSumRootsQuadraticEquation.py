from math import sqrt 
def roots(a,b,c):     
    
    discriminante = ((b**2) - (4*a*c))
    denominador = 2*a
    
    if discriminante < 0 or denominador == 0: return None
    

    print(discriminante)
    return round(((-(b)- sqrt(discriminante))/denominador)+((-(b)+ sqrt(discriminante))/denominador), 2)
    

