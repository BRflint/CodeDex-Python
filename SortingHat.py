# Write code below 💖
#declare variables
gryffin = int(0)
raven = int (0)
huffle = int (0)
sly = int(0)
#questions 1
print("Q1) do you like dawn or dusk?")
print("1)dawn")
print("2)dusk")
ans1 = int(input())

#First question input
if ans1 == 1:
  gryffin = gryffin + 1 
  raven = raven + 1
elif ans1 == 2:
  huffle = huffle + 1
  sly = sly + 1
else:
  print("wrong input")

#2nd question
print("when i'm dead, i want people to remember me as: ")
print("the good")
print("the great")
print("the wise")
print("the bold")
ans2= int(input())
#2nd question input

if ans2 == 1:
    huffle = huffle + 2 
elif ans2 == 2:
    sly = sly + 2
elif ans2 == 3:
    raven = raven + 2
elif ans2 == 4:
    gryffin = gryffin + 2
else:
  print("wrong input")

#Q3 
print("which kind of instrument most pleases your ear? ")
print("1) the violin")
print("2) the trumpet")
print("3) the piano")
print("4) the drum")
ans3 = int(input())

#Q3 response
if ans3 == 1:
    sly = sly + 4
elif ans3 == 2:
    huffle = huffle + 4
elif ans3 == 3:
   raven = raven + 4
elif ans3 == 4:
    gryffin = gryffin + 4
else:
  print("wrong input")


#calculations
if gryffin >= raven and gryffin >= huffle and gryffin >= sly:
  print('🦁 Gryffindor!')
elif raven >= huffle and raven >= sly:
  print('🦅 Ravenclaw!')
elif huffle >= sly:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
