
number1 = input('Enter an integer: ')

while type(number1) != int:
    try:
        number1 = int(number1)
    except:
        number1 = input('Please enter again: ')

    if type(number1) != int:
        print('the number is not integer')
    else:
        print('the number is integer')

print(number1)