# Find all occurrences of a substring in a given string by ignoring the case

# str1 = "Welcome to USA. usa awesome, isn't it?"
# count of usa=2


def count_substr(str1,sub_str):

    str_temp=str1.split()

    count=str_temp.count(sub_str)

    return count
print(count_substr("happy happy usa happy haiii","happy"))





# Exercise 15: Remove special symbols / punctuation from a string


# regular expression is needed







str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)