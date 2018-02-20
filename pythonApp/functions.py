#Functions
from Crypto.Util import _number_new
from Crypto.SelfTest.Util import test_number
from variables import myList

#def is used to define a function

def sayHello():
    print("Hi")
    
#call function
sayHello()

def sayHello2(name):
    'Print hello to name'  #This is also comment
    print("Hi", name)
    
#call function
sayHello2('John')

def getSum(num1, num2):
    total = num1+num2
    return total

numSum = getSum(2, 3)
print(numSum)

print(getSum(-1, 10))
print(getSum('a', 'b'))
print(getSum("a", 'b'))
print(getSum('10', 'b'))


#Imutable data cannot be changed by can be overwritten like string and ints are immutables but dict is mutable

def addOneToNum(num):
    num = num + 1; #This doesn't change the num out side the fucntion as num is immutable
    print("Value inside the function", num)
    return

num=5
addOneToNum(num)
print("Value outside the function", num)


def addOneToList(list):
    list.append(4)      #This will change list as list is mutable
    print("List inside function", list)
    return

myList = [1,2,3]
addOneToList(myList)
print("List outside function", myList)


