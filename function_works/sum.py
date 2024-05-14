# add 2 number
def add(num1,num2):
    res=num1+num2
    return res
out=add(100,200)
print(out)
# print(add(100,200))

# add 3 numbers
def add_three(n1,n2,n3):
    res=n1+n2+n3
    print(res)
add_three(2,4,6)

# find cube
def cube(n1):
    res=n1**3
    return res
print(cube(5))


# checking the number +ve or not
def num_check(num):
    res= "+ve" if num>0 else "-ve" if num<0 else "zero" 
    return res   
print(num_check(9))