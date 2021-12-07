def take_float_input(msg):
    a=input(msg)
    while type(a) != float :
        try :
            a = float(a)
            return a
        except : 
            a = input("Please give a valid input :")

Num1 = take_float_input("Please enter a number :")

Num2 = take_float_input("Please enter another number :")

print("The availabe actions are : +, -, *, / ")
Action = input("Please choose an action :")


    

if Action=='+' :
    R = Num1 + Num2
    print(f"The summition of the numbers is : {R}")
elif Action =='-' :
    R = Num1 - Num2
    print(f"The subtraction of the numbers is : {R}")
elif Action =='*' :
    R = Num1 * Num2
    print(f"The multiplication of the numbers is : {R}")
elif Action =='/' :
    R = Num1 / Num2 
    print(f"The quotient of the numbers is : {R}")
else :
    print("How did you get to this point?")

input("Please press enter to exit.")