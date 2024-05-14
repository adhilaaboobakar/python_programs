weight_inkg = int(input("enter weight in kg"))
heightin_cm = int(input("enter height in cm"))

heightin_meter = heightin_cm/100

bmi = weight_inkg/heightin_meter**2
print(bmi)

if bmi<19:
    print("underweight")
elif bmi<25 :
    print("healthy")
elif bmi<30:
    print("overweight")
elif bmi<40:
    print("obesity")
else:
    print("severe obese")