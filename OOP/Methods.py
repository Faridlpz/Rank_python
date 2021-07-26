class Parrot:

    #instance attributes
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    #instance method || se usa para definir el comportamiento de un objeto
    def sing(self,song):
        return "{} sing {}".format(self.name,song)

    
# instantiate the object
blue = Parrot("blue", 10) #blue es un objeto de mi clase Parrot

#call our instance methods
print(blue.sing("happy"))