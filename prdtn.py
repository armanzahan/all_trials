print ("This is a programme for calculaiting the productin capacity of a machine")

D = input ("Please enter the machine dia :")
g = input ("Please enter machine gauge :")
F = input ("Please enter the number of feeders :")
SL = input ("Plese enter the Stitch length :")
r = input ("Plese enter the rpm :")
t = input ("Plese enter the time (seconds) : ")
C = input ("Please enter Yarn count (Ne) :")

D = int(D)
g = int (g)
F = float (F)
SL = float (SL)
r = int (r)
t = int (t)
C = int (C)
E = 1 
E = float (E) 

PC = (3.1416*D*g*F*SL*r*t*1.09) / (1000*C*840*2.2046)

print (f"The production capacity is (kg) : {PC} ")
input ("Press enter to exit.")
