#STRING FUNCIONS

#Remember string is immutable so all operations below will not change the variable myStr itself
myStr = 'Hello World'

print(myStr.capitalize())
print(myStr.swapcase())
print(myStr[0].swapcase())
print(len(myStr))
print(myStr.replace('World', 'Everyone'))
sub="l"
print(myStr.count(sub)) #Count substrings

#check if the string starts with specific sub str
print(myStr.startswith('Hello'))
print(myStr.endswith('world'))  #false
print(myStr.endswith('World'))  #true

print(myStr.split())
print(myStr.find('e'))  #return index of first occurence of e
print(myStr.find('l'))  #return index of first occurence of e
print(myStr.find('x'))  #return -1 as no x

print(myStr.isalnum())  #will return false as space between Hello and World is no alphanumeirc
print(myStr.replace(' ', '').isalnum()) #remove space and then check and it will return true

print(myStr.isalpha())  #Will return false as it's not all alphanetic due to space char
print(myStr.replace(' ', '1').isalpha()) #replace space with num and still it will be false
print(myStr.replace(' ', '').isalpha()) #remove space and still it will be true

