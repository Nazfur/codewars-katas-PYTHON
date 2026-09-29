def well(x):
    
    cantidad_buenas_ideas = x.count("good")
    if cantidad_buenas_ideas > 2:
        return "I smell a series!"
    elif cantidad_buenas_ideas >=1:
        return "Publish!"
    else:
        return "Fail!"

