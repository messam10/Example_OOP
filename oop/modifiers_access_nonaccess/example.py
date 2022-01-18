class Father: # super class
    a = None
    _b = None
    __c = None

    def __init__(self, a, b, c):
        self.a = "Hi"
        self.b = "Hello"
        self.c = "Hola"
    
    def showFather(self):
        print("class Father : public ",self.a)
        print("class Father : protected ",self.b)
        print("class Father : private ",self.c)
    
    def _show(self):
        print("class Father : public ",self.a)
        print("class Father : protected ",self.b)
        print("class Father : private ",self.c)

class Son(Father): # sub class
    def __init__(self, a, b, c):
        Father.__init__(self, a, b, c)

    def showSon(self):
        print("class Son : public ",self.a)
        print("class Son : protected ",self.b)
        print("class Son : private ",self.c)


class Friend: # class
    def __init__(self, a, b, c):
        Father.__init__(self, a, b, c)

    def showFriend(self):
        print("class Frind : public ",self.a)
        print("class Frind : protected ",self.b)
        print("class Frind : private ",self.c)
    


s = Son("Hi a", "Hi b", "Hi c") # object
s._show()
s.showFather()
s.showSon()
print(s.a)
print(s.b)
print(s.c)

f = Friend("Hi a", "Hi b", "Hi c")
f.showFriend()
# f._show() Error
# f.showFather() Error
# f.showSon() Error
