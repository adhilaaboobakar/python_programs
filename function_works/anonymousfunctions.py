# lamba function is used when there is only one line.used instead of normal function. To consise the function

# for addition

add=lambda n1,n2:n1+n2
print(add(10,20))

# find cube

cube =lambda n1:n1**3
print(cube(3))

# number check +ve or not

# de num_check(num):
#     return "+ve" if num>0 else "-ve"
#     

num_check =lambda num:"+ve" if num>0 else "-ve" if num<0 else"zero"
print(num_check(3))

# print largest among two

max_two= lambda n1,n2:n1 if n1>n2 else n2
print(max_two(4,9))

# odd or even
odd_even = lambda num:"even" if num%2==0 else"odd"
print(odd_even(9))

text = "good evening all"
words= text.split(" ")
srt_words = sorted(words)
srt_words= sorted(words,key = lambda w:len(w),reverse=True)
print(srt_words)

num=10,20,30
print(num)





    
