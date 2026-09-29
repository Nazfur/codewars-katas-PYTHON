def evil(n):

    sumatorio = 0 
    
    for i in bin(n)[2:]:
        if i == '1':
            sumatorio += 1
    
    if sumatorio % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
