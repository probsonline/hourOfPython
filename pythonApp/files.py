#Open a file

fo = open('test.txt', 'w')

#get some info
print('Name: ', fo.name)
print('Is close:', fo.closed)
print('Opening mode:', fo.mode)

fo.write('I love python\n')
fo.write(' I love java') #This will append as file i not yet closed
fo.closed

fo = open('test.txt', 'w')  #again open in write mode
fo.write('I also like PHP') #this will overwrite file by these contents but if the file contains more than this can overwrite, that will remain there. To avoid these problems open in append mode
fo.close()

fo = open('test.txt', 'a')
fo.write(' Whatever it is I am starting')
fo.close

fo = open('test.txt', 'r+')
text = fo.read(10)  #read 10 character
print(text)
fo.close

fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close