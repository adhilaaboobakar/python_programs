# Write a program to print 10,8,6,4,.....-6,-8,-10

# i=10
# while(i>=-10):
#     print(i)

#     i-=2



# Write a program to print sum of even number in a range

# start=int(input("Enter the start value : "))
# end=int(input("Enter the end value : "))
# sum=0
# for i in range(start,end):
#     if i%2==0:
#         sum+=i
        
# print(sum)



# Write a program to calculate BMI and give message "overweight,underweight,normal"

weight_kg=int(input("Enter your weight in kg "))
height_cm=int(input("Enter your height in cm "))
hght_m=height_cm/100

bmi=weight_kg/hght_m**2
print(bmi)

if bmi<19:
    print("underweight")
elif bmi<25 :
    print("normal")
elif bmi<30:
    print("overweight")
else:
    print("obesity")