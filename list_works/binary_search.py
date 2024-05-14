lst=[5,8,3,6,9,2,7]

lst.sort()

element=int(input("enter a number"))

low=0
upp=len(lst)-1
is_present=False

while(low<=upp):
    mid=(low+upp)//2

    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upp=mid-1
    elif element>lst[mid]:
        low=low+1
print(is_present)

