# find common elements from the two list

lst=[9,4,3,10,15]
lsts=[5,4,2,3,20]

# for num in lst:
#     if num in lsts:
#         print(num)


lst.sort()
lsts.sort()

p1,p2=0,0
while(p1<len(lst)) and p2<len(lsts):
    if lst[p1]==lsts[p2]:
        print(lst[p1])
        p1+=1
        p2+=1
    elif lst[p1]<lsts[p2]:
        p1+=1
    else:
        p2+=1
