# create a string made up of first last and middle of  these characters


text="hello"


last=len(text)-1
middle=int(len(text) /2)

res=""

res=text[0]+text[middle]+text[last]
print(res)



# create a string made of the middle 3 characters


text="morning"


mid=int(len(text) /2)

res=""

res=text[mid-1:mid+2]

print(res)



# : Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.


# Expected Output:  AuKellylt


s1 = "Ault"
s2 = "Kelly"

s3=""
mid=int(len(s1) /2)

s3=s1[:mid]+s2+s1[mid:]
print(s3)




# Create a new string made of the first, middle, and last characters of each input string


# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.


# s1 = "America"
# s2 = "Japan"
# Expected Output:AJrpan



def two_string(s1,s2):

    s3=s1[0]+s2[0]
    s1_mid=int(len(s1) /2)
    s2_mid=int(len(s2) /2)
    s1_last= len(s1)
    s2_last= len(s2)
    s3=s3+s1[s1_mid]+s2[s2_mid]+s1[s1_last-1]+s2[s2_last-1]
    return s3

print(two_string("America","Japan"))




