num = int(input("enter a number"))

if num%3 ==0 and num%5 == 0:
    print("fizzbuzz")
elif num%5 == 0 :
    print("buzz")
elif num%3 ==0 :
    print("fizz ")
else:
    print("not divisible by 3 or 5")


# num%15 == 0
# print("fizzbuzz") in first