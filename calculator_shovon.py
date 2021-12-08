def take_float_input(msg):
    a = input(msg)
    while type(a) != float:
        try:
            a = float(a)
            return a
        except:
            a = input('You didn\'t entered an float value.')


instructions = [
    'What kind of operation do you want to make? Enter one of the symbols:',
    '+ for Addition,',
    '- for Subtraction,',
    '* for Multiplication and',
    '/ for Division\n'
]

operation_symbol = input('\n'.join(instructions))

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
