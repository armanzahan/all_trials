def take_int_input(msg):
    a = input(msg)
    while type(a) != int:
        try:
            a = int(a)
            return a
        except:
            a = input('You didn\'t entered an integer.')

def take_float_input(msg):
    a = input(msg)
    while type(a) != float:
        try:
            a = float(a)
            return a
        except:
            a = input('You didn\'t entered an float value.')


D= take_int_input("Please enter the diameter :")
g = take_int_input ("Please enter machine gauge :")
F = take_int_input ("Please enter the number of feeders :")
SL = take_float_input ("Plese enter the Stitch length :")
r = take_int_input ("Plese enter the rpm :")
t = take_int_input ("Plese enter the time (minutes) : ")
C = take_int_input ("Please enter Yarn count (Ne) :")
PSP = take_int_input ("please enter  previous shift production (kg) :")

D=int(D)
g = int (g)
F = int (F)
SL = float (SL)
r = int (r)
t = int (t)
C = int (C)
PSP = float (PSP)




E= (10*2.54*36*2.2046*840*C*PSP*100)/(3.1416*SL*r*t*D*g*F)

print(f"Efficiency = {E} % ")

if E<70 :
    print("the machine has not achieve it's target.")
elif E == 70:
    print('The machine has achieved the target.')
else :
    print("The machine has exceeded it's target.")

E = 0.70
E = float (E)

PT = (3.1416*D*g*F*SL*r*t*1.09*E) / (1000*C*840*2.2046)

print (f"The production Target is (kg) : {PT} ")
input (" press enter to exit.")