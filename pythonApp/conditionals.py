#Conditionals


"""
no () or {} in python for blocks. rather : and indentation are the key
"""

x = 4
name = "Kaleem"

if x < 5 and x > 0 and name=="Kaleem":
    print("true")
    print("I am ", name)
#print("Who are you")        #This will not work as the indentation is not the same so it will fail to interpret
elif x<0:
    print ("Invalid input")
else:
    print("x is greater than 5")