
def getRad(radical): 
    printI = False                                                                                                                                           
    works = False                                                                                                                                            
    if radical < 0:                                                                                                                                          
        radical *= -1                                                                                                                                        
        printI = True                                                                                                                                        
    persq = [4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]                                                                              
    for num in persq[::-1]:                                                                                                                                  
        if radical == num:                                                                                                                                   
            string = str(radical ** 0.5)                                                                                                                            
            works = True                                                                                                                                     
            break                                                                                                                                            
        if radical % num == 0:                                                                                                                               
            if printI == True:                                                                                                                               
                string = (str(num ** 0.5)+"i√"+str(radical/num))                                                                                                           
            else:                                                                                                                                            
                string = (str(num ** 0.5)+"√"+str(radical/num))                                                                                                            
            works = True                                                                                                                                     
            break              
    if works == False:        
        return str(radical)
    return string
