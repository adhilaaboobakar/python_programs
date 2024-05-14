lst=[2,4,6,7,8]

search_num=int(input("enter a number"))

is_present=False
for i in range(0,len(lst)):
    if lst[i]== search_num:
        is_present=True
        break
print(is_present)