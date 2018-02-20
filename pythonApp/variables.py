#VARIABLES and DATA TYPES

greeting = 'Hello World'
greeting = 'Hello Everyone' #Just reassignng greeting

print(greeting)
#DATA Types
myStr = 'Hello'
myInt = 25
myFloat = 1.3

myList = [1,2,3,'Hello']
myDict = {'a':1, 'b':2, 'c':3}   #Key value pairs

#print the type of the variable and the variable value
print(type(greeting))
print(type(myStr), myStr)
print(type(myInt), myInt)  
print(type(myFloat), myFloat)  
print(type(myList), myList)  
print(type(myDict), myDict)  
 
print(myList[3]) #specify the index in the list
print(myDict['a']) #Specify key and and it will print its value

#string concatentation
print(myStr, 'World')
greeting = myStr + 'World'
print(greeting)