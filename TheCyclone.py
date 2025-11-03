height = int(input("please enter your height: "))
credit = int(input("now please enter credits: "))

if height >= 137 and credit >= 10:
    print("enjoy the ride!")
elif height < 137 and credit >=10:
    print("you are not tall enough to ride.")
elif height >= 137 and credit < 10:
    print("you dont have enough credits.")
elif height < 137 and credit <10:
    print("you have not meet either requirement.")