from random import randint

def colorAleatorio():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0, 255)

    return (r,g,b)

def posicionAleatoria():
    x = randint(0,800)
    y = randint(0,600)
    return [x,y]