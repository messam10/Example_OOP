class Father: # super class
    def speack(self):
        print("Speack Arabic")

    def defFather(self):
        print("class father")

class Mother: # super class
    def speack(self):
        print("Speack English")

    def defMother(self):
        print("class mother")

class Son(Father, Mother): # sub class
    def speack(self):
        print("try to speak")

    def defSon(self):
        print("class son")

s = Son() # object
s.speack() # will print in sub class if function not found will print in super class "Father"
s.defFather() # will print in super class father
s.defMother() # will print in super class mother
s.defSon() # will print in sub class