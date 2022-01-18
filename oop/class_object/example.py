class Person: # class
    age = 10

    def greet(self):
        print('Hello')


mohammed = Person() # object
print("Person.greet - ",Person.greet)
print("mohammed.greet -",mohammed.greet)
print("mohammed.greet() -",mohammed.greet())