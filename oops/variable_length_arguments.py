
# def addition(*args):
#     return sum(args)

# print(addition(10,20))
# print(addition(10,20,30))


# def product(*args):
#     result=1
#     for n in args:
#         result=result*n
#     return result
    
# print(product(10,20))

# last_digit sum
def last_digit_sum(*args):
    result=0
    for n in args:
        last_digit=n%10
        result+=last_digit
    return result

print(last_digit_sum(123,342,10,57))


# last_digit_max

# def last_digit_max(*args):
#     last_digit=[n%10 for n in args]
#     print(last_digit)
#     return max(last_digit) 


# print(last_digit_max(12,345,78))   


# # **kwargs takes as dict but *args takes as tuple

# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))

# add_employee(id=10,name="hari",n_place="ekm",w_place="tvm",salary=24000)



# last_digit_calculator(12,34,56,op=)