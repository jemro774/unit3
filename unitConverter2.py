#Jack Robey
#10/2/17
#unitConverter2.py - unitConverter.py + the ability for the user to quit and for the program to start over after a calculation

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celcius to Fahrenheit')
print('5) Quit')

num = int(input('Choose a unit conversion by entering in one of the displayed numbers: '))

if num == 1:
    km = float(input('Enter the amount of kilometers: '))
    print('There are', round(km*0.62137119223733, 2), 'miles in', km, 'kilometers')
elif num == 2:
    kg = float(input('Enter the amount of kilograms: '))
    print('There are', round(kg*2.2046226218488, 2), 'pounds in', kg, 'kilograms')
elif num == 3:
    li = float(input('Enter the amount of liters: '))
    print('There are', round(li*0.26417205235815, 2), 'gallons in', li, 'liters')
elif num == 4:
    cel = float(input('Enter a temperature in celcius: '))
    print(cel, 'degrees Celcius is equal to', round(cel*1.8+32, 2), 'degrees Fahrenheit')
elif num == 5:
    break
else:
    print('Error, invalid number entered')
