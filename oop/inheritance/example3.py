class GrandFather: # super class
    def speack(self):
        print("Speack Arabic")

    def defFather(self):
        print("class GrandFather")

class Father(GrandFather): # super class to Son && sub class to GrandFather
    def speack(self):
        print("Speack English")

    def defMother(self):
        print("class Father")

class Son(Father): # sub class
    def speack(self):
        print("try to speak")

    def defSon(self):
        print("class son")

s = Son() # object
s.speack() # will print in sub class if function not found will print in super class "Father"
s.defFather() # will print in super class GrandFather
s.defMother() # will print in super class Father
s.defSon() # will print in sub class