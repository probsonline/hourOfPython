#CLASSES and OBJECTS
#classes can hold properties and functions/methods
class Person:
    __name = '' #__ represents that it's private and can't be accessed outside class
    __email = ''
    
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    #Define getter/setters to access private members
    def set_name(self, name):   #Self is same as this in Java/c++
        self.__name = name
        
    def set_email(self, email):
        self.__email=email
        
    def get_name(self):   #Self is same as this in Java/c++
        return self.__name
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        '{} is the place holder for the variable specified later'
        return '{} can be contacted at {}'.format(self.__name, self.__email)

'''    
brad = Person("Brad Traversy", "brad@gmail.com")
print(brad.get_name())
print(brad.get_email())
print(brad.toString())
'''
#inheritance. instead of using the word extends simply put the name of the class to be extended as param
class Customer(Person):
    __balance = 0
    
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        
    def set_balance(self, balance):
        self.__balance=balance
        
    def get_balance(self):   #Self is same as this in Java/c++
        return self.__balance
        
    def toString(self):
        return '{} has a balance of {} can be contacted at {}'.format(self.__name, self.__balance, self.__email)


john = Customer('John Doe', 'john@gmail.com', 100)
print(john.toString())

john.set_balance(400)
print(john.toString())

kate = Customer('Kate Smith', 'kate@gmail.com', 5000)
print(kate.toString())