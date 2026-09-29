def clicker_solver(up, goal) -> int:
    
    if goal <= 0: return 0
    if up <= 0: return -1

    
    numero_clicks = 0
    cpc = up
    
    while True:
        if ((cpc**2) + (goal/(cpc+up))) < (goal/cpc):
            numero_clicks += cpc**2 + 1
            cpc += up
            
        else:
            numero_clicks += -(-goal//cpc)
            return numero_clicks

