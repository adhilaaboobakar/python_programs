# print all leap years from starting year to current year
starting_year = int(input("enter a year"))
current_year = 2023

i=starting_year
while(i<=current_year):
    if i%100 ==0 and i%400 ==0 or i%100!=0 and i%4==0:
        print(i)
    i+=1


    