#static and class methods #2

class Person(object):
    population = 50
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age = age
    
    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'year old')

newPerson = Person('tim',18)

print(Person.getPopulation())
