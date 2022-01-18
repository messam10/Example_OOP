class ComplexNumber: # class
    def __init__(self, r=0, i=0): # constructor
        self.real = r
        self.imag = i
    
    def __del__(self): # destructor
        print("Destructor called, vehicle deleted.")
    
    def get_data(self):
        print("{}+{}j".format(self.real,self.imag ))


num = ComplexNumber(2, 3) # object with constructor
num.get_data() # call function
print(num.real) # after the functions are performed __del__ is called directly and automatically
num.__del__() # call destructor again