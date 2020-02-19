#Example 1:
#in python a class is created with a keyword 'class' followed by the name of the class
#in this case its 'Animal'
#every class has to have the '__init__' method. Thats sort of the 'Constructor' of the class
#the class has the variable 'name' although it hasn't been defined as one, but its used in the constructor and it's initialized
#the class also has functions of its own. 'getName' is one such function
#in python, every function of the class has to have 'self' as its 1st argument/parameter which can then be followed by
#any other parameter
class Animal:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

#creating an object or instance of the class Animal
dog = Animal('Rex')

# 'dog' can now access all the variables and functions in the 'Animal' class
print(dog.name) #(o/p) → Rex

#accessing and changing the value in the 'name' variable
dog.name = 'Tyler'
full_name = dog.getName()   #notice how we don't pass anything in this parameter when calling it

#both the outputs will be the same. Both will print 'Tyler'
print(dog.getName())
print(full_name)


#Example 2:
#in this class, the 'Person' has 2 attributes 
class Person:
    attribute_1 = 'tall'
    attribute_2 = 'short'

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    #we can access the class attributes through the dot operator and display them
    def describe(self):
        print('My name is', self.name, 'and I am', self.attribute_1)
        print('My name is not', self.getName(),
              'and I am', self.attribute_2)


Aaron = Person('Aaron')
Aaron.describe()

Aaron.name = 'Leander'
Aaron.describe()

Aaron.name = 'Ibrahim Parkar'
#we can also change the value of the attribute. However, the attribute will change for only that object of the class
#and not for all the objects of the class
Aaron.attribute_1 = 'awesome'
Aaron.attribute_2 = 'not awesome'
Aaron.describe()
print(Aaron.attribute_1)    #the (o/p) → awesome

Aldair = Person('Aldair')
Aldair.describe()
print(Aldair.attribute_1)   #the (o/p) → tall
