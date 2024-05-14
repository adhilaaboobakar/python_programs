# print the squares of the list as another list

lst=[2,4,5,6,7,8,9]

squares=[]
for num in lst:
    sq=num**2
    squares.append(sq)
print(squares)

# make a seperate list for even numbers from the given list

lst=[2,4,5,6,7,8,9]
evens=[]

for num in lst:
    if num%2==0:
        evens.append(num)

print(evens)


# list comprehension - [ return value taking the numbers condition]
# square?

lst=[2,3,4,5,6,7,8,9]
squares=[ num**2 for num in lst ]
print(squares)

cubes=[num**3 for num in lst]
print(cubes)

evens= [num for num in lst  if num%2==0]
print(evens)

num_gt_five=[ num for num in lst if num>5]
print(num_gt_five)

# make capital letters

words=["apple","orange","banana","mango","potato"]

upper=[word.capitalize() for word in words]
print(upper)

# print names whose length>4
names=["manoj","akshay","rahul","arju"]
num_gt_four=[ name for name in names if len(name)>4]
print(num_gt_four)