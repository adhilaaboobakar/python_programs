# print all non-century year from starting year to current year

starting_year =int(input("enter a year"))
current_year = 2023

i=starting_year
while(i<current_year):
    if i%100!=0:
        print(i)
    i+=1
