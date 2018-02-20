#This is a single line comment
'''
This is a multi line comment
'''
"""
This is also a multi line comment
"""
#Stay consistent with your quotes
#Single Quote
print('In the name of Allah, I start to learn python')

#Double Quote
print("In the name of Allah, I start to learn python")

print("""Heloo""")

#Print substrings
print('Hello'[0])
print('Hello'[0:3])
print(1,2,3,'Hello')    #Can print numbers and strings together
print('Line1\nLine2\nLine3')
print(r'c:\\somewhere\n') #r indicates to treat \n as regular character and nto the new line special chrater

#{} together for the function .format can be using on string to replace {} with the paramters of format
print('{} is my number'.format(5))