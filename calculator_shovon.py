def take_float_input(msg):
    a = input(msg)
    while type(a) != float:
        try:
            a = float(a)
            return a
        except:
            a = input('You didn\'t entered an float value.')


# Print the complete message with instructions so that user doesn't make mistake
print('What kind of operation do you want to make? Enter one of the symbols:')
print('+ for Addition,')
print('- for Subtraction,')
print('* for Multiplication and')
print('/ for Division')
operation_symbol = input()

# Validate the input
while operation_symbol != '+' and operation_symbol != '-' and operation_symbol != 'x' and operation_symbol != '/':
    operation_symbol = input('Please enter a valid symbol: ')

# Take the number inputs and also validate the operation symbol
while True:
    if operation_symbol == '+':
        number1 = take_float_input('Enter a number: ')
        number2 = take_float_input('Enter another one: ')
        result = number1 + number2
        break
    elif operation_symbol == '-':
        number1 = take_float_input('Enter the minuend: ')
        number2 = take_float_input('Enter the subtrahend: ')
        result = number1 - number2
        break
    elif operation_symbol == '*':
        number1 = take_float_input('Enter the multiplicand: ')
        number2 = take_float_input('Enter the multiplier: ')
        result = number1 * number2
        break
    elif operation_symbol == '/':
        number1 = take_float_input('Enter the dividend: ')
        number2 = take_float_input('Enter the divisor: ')
        result = number1 / number2
        break
    else:
        operation_symbol = input('Please enter a valid symbol: ')

print(f'The result is {result}')
