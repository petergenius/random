
def solveSystem(a1,a2,b1,b2,c1,c2):
    a = a1 - a2                                                                                                                                              
    b = b1 - b2                                                                                                                                              
    c = c1 - c2                                                                                                                                              
    x1 = ((-1 * b) + ((b**2) - (4* a * c)) ** 0.5)/2 * a                                                                                                     
    x2 = ((-1 * b) - ((b**2) - (4* a * c)) ** 0.5)/2 * a                                                                                                     
    y1 = (a1 * x1 * x1) + (b1 * x1) + c1                                                                                                                     
    y2 = (a1 * x2 * x2) + (b1 * x2) + c1                                                                                                                     
    coords = "("+str(x1)+","+str(y1)+")"                                                                                                                                 
    coords2 = ("("+str(x2)+","+str(y2)+")"     
    return coords, coords2
