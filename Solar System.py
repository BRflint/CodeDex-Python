# Write code below 💖

from math import pi
from random import choice as ch

#list
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
radius = [2440,6052,6371,3390,58232]
#variables
random_planets = ch(planets) # confirmed

area = 4 * pi ** 2



if random_planets == 'Mercury':
 result = radius[0]* area

 print(result)
  
elif random_planets == 'Venus':
 result = radius[1]* area

 print(result)
  
elif random_planets == 'Earth':
 result = radius[2]* area

 print(result)
  
elif random_planets == 'Mars':
 result = radius[3]* area

 print(result)
  
elif random_planets == 'Saturn':
 result = radius[4]* area

 print(result)

else:
 print("sorry not working try again")
