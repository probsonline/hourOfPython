#If from is not used and just import is used whole module is imported

#import entire module
import greet
greet.sayHello('Tim')

#or import a part of the module using from 'module, import
from greet import sayGoodBye
greet.sayGoodBye('Tim')
