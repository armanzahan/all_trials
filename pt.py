D= input("Please enter the diameter :")
g = input ("Please enter machine gauge :")
F = input ("Please enter the number of feeders :")
SL = input ("Plese enter the Stitch length :")
r = input ("Plese enter the rpm :")
t = input ("Plese enter the time (minutes) : ")
C = input ("Please enter Yarn count (Ne) :")
PSP = input ("please enter  previous shift production (kg) :")

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

while E == 70  :
    print("The machine has achieved it's target!")
if E<70 :
    print("the machine has not achieve it's target.")
else :
    print ("The machine has exceeded it's target.")

E = 0.70
E = float (E)

PT = (3.1416*D*g*F*SL*r*t*1.09*E) / (1000*C*840*2.2046)

print (f"The production Target is (kg) : {PT} ")
input (" press enter to exit.")
