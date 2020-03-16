# create class


class Dog:

    # class attribute
    species = 'mammal'

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return 'Instance method:-- Dog name: %s , Dog age: %i' %(self.name, self.age)


# instantiate an object

simba = Dog("Simba", 6)

# access object 
print('Dog name: %s , Dog age: %i' %(simba.name, simba.age))

# using instance methods
print(simba.description())

# child class

class Bulldog(Dog):

    def speed(self, speed):
        return '%s runs at %i km/h' %(self.name, speed)

bruno = Bulldog('Bruno', 5)
print(bruno.speed(20))