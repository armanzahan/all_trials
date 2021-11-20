print("Please enter the following informations :" )

C = input("Enter Count :")
C =  int(C)

P = input("Enter production :")
P =  int(P)

S = input("Enter stitch length :")
S = float(S)

r = input("Enter rpm :")
r =  int(r)

t = input("Enter time:")
t = int(t)
D = input("Enter diameter :")
D =   int(D)

g = input("Enter Machine gauge :")
g =  int(g)

F = input("Enter number of feeders :")
F = int(F)

E= (10*2.54*36*2.2046*840*C*P*100)/(3.1416*S*r*t*D*g*F)

print(f"Efficiency = {E} % ")

input("press enter to exit")