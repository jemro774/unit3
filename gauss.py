#Jack Robey
#9/29/17
#gauss.py - uses a loop to add up all the numbers from 1 to 100

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
diff = int(input('Enter a difference: '))

total = 0
for i in range(num1,num2+1,diff):
    total += i
print(total)
