class Father: # super class
    def __init__(self): # constructor
        self._a = 2
 
class Son(Father): # sub class
    def __init__(self): # constructor
        Father.__init__(self)
        print("Number Befor Change ",self._a)
        
        self._a = 3
        print("Number After Change  ",self._a)
 
 
s = Son() # object
f = Father() # object
print("Number in Class Son ", s._a)
print("Number in Class Father ", f._a)