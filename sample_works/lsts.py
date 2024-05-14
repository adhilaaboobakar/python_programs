
# largest element in the list

lst=[6,68,56,89,9]

max_num=max(lst)
print(max_num)
print(len(lst))
print(lst[4])
# remove duplicate numbers

lst=[2,5,6,2,7,8,3,5]

set_nums=set(lst)
print(set_nums)

# find the duplicate numbers

lst=[2,3,2,4,5,2,5,3]

duplicates=[]
for num in lst:
    if lst.count(num)>1 and  num not in duplicates:
        duplicates.append(num)
print(duplicates)



# last element in the list


# sum of the squares of the natural numbers in the array

arr=[1,2,3,4,5]


squares=sum([num**2 for num in arr])
print(squares)
square_sum=[]