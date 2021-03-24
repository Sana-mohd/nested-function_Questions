def outerFunction(text): 
    text = text 
    
    def innerFunction(): 
        print(text) 
    
    return innerFunction 
    
if True : 
    myFunction = outerFunction('Hey !') 
    myFunction() 
