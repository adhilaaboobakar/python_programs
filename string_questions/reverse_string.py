# input="hello"
# output="olleh"


# def reverse_string(input):
#     return input[::-1]


# mytxt=reverse_string("hello")
# print(mytxt)


def string_reverse(input):
    reversed_string= ""
    for char in input:
        reversed_string=char+reversed_string
    return reversed_string
    
print(string_reverse("hello"))
