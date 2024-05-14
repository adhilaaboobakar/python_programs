

company="LUMINAR"    #actually company is a string object.bcoz it shows in double quotes.so it takes as string object.basically we tell its variable
print(company.casefold()) #convert uppercase to lowercase
print(company.capitalize()) #convert first character to uppercase
print(company.lower()) #convert all characters to lowercase
print(company.upper()) # convert all characters to upper
print(company.isalpha())#if only alphabets written true

com="ababcdbacd"
print(com.isdigit()) #print true when all are digits
print(com.isalnum())#whether alphabet or number print true

word="nhellooon"
print(word.strip("n"))# remove the character from only from the left and right side of the target string.
wo="helloi"
print(wo.rstrip('i'))
# rstrip() = from right side
# lstrip()
# print(company.lstrip('r'))


home="hello company football"
words=home.split()
print(words)