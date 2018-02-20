#LOOPS

#For LOOP

people = ['John', 'Sara', 'Tim', 'Bob']

for person in people:
    print('Current person', person)
    
#iterate by seq index
for i in range(len(people)):
    print('Current person', people[i])
    
for i in range(0, 10):
    print(i)    
    
#WHILE LOOP
count=0
while count < 10:
    print('Count', count)
    count = count +1;
    if count == 5:
        break;
    
