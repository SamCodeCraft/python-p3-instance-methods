class Person:
    
    def talk(self):
        print("Hello World!")
        
    def walk(self):
        print("The person is walking.")

# Create an instance of the Person class outside the class definition
guido = Person()

# Call the instance methods
guido.talk()
guido.walk()
