def take_float_input(msg):
    a = input(msg)
    while type(a) != float:
        try:
            a = float(a)
            return a
        except:
            a = input('You didn\'t entered an float value.')


radius = take_float_input('Enter radius: ')

area_of_circle = 3.1416 * radius * radius
print(f'The area of the circle is {area_of_circle}')

if area_of_circle < 30:
    print('Vai hoy nai.')
elif area_of_circle == 30:
    print('Vai shei vai shei')
else:
    print('Vai ektu beshi hoye gelo na?')