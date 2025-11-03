#input
Co = int(input("enter the amount of Colombian Pesos you have: " ))
Pe = int(input("now Preuvian Soles: " ))
Br = int(input("finally Brazilian reais" ))

#calculation
Usd = (Co * .00025) + (Pe * .28) + (Br * .18)

#prints 
print ("your total amount is: ")
print (Usd)