import random
num = random.randint(1,8)

#input
Question = input("What would you wish to know? ")

#ball response
if num == 8:
    print("Yes - definitely.")
elif num == 7:
    print("It is decidedly so.")
elif num == 6:
    print("Without a doubt")
elif num == 5:
    print("Reply hazy, try again.")
elif num == 4:
    print("Ask again later")
elif num == 3:
    print("Better not tell you now.")
elif num == 2:
    print("My sources say no.")
elif num == 1:
    print("Outlook not so good")
print(num)