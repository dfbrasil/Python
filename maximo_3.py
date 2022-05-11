def maximo(x,y,z):

    if x>y and x>z:
        i = x
    elif y>x and y>z:
        i = y
    else:
        i = z
    return(i)
