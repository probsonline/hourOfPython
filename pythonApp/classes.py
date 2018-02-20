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
    

#Let's use the class now by creating objects
"""
brad = Person() #as long as the constructor is not defined, the default constructor without any arguments will work
brad.set_name('Brad Traversy')
brad.set_email('brad@gmail.com')


#print(brad.__email)    This will not work as email is prinvate
print(brad.get_email())
"""
brad = Person("Brad Traversy", "brad@gmail.com")
print(brad.get_name())
print(brad.get_email())
print(brad.toString())
