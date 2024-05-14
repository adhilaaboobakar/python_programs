name="TECHNOLAB"

# slicing [start:stop:step]
# print(name[2:])
print(name[:7])
print(name[6:8])


print(name[-1:-4:-1])

print(name[:-5:-1])

# word="madam"

# reverse_string=word[::-1]

# print("palindrome" if word==reverse_string else "not palindrome")

# str1="hello"
# str2="goodmorning"

# str1_length=len(str1)
# # print(str1_length)

# rem=str2[str1_length:]
# print(rem)



string1=input("enter string1: ")
string2=input("enter string2: ")


smallest_length=min(len(string1),len(string2))
result=""
for i in range(0,len(string1)):
    out=string1[i]+string2[i]
    result+=out
if len(string1)>len(string2):
    rem=string1[smallest_length:]
else:
    rem=string2[smallest_length:]
result+=rem
print(result)


