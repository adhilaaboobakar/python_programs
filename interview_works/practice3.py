


text="hellohaii"

# print the vowels in text without duplicates


vowels=["a","e","i","o","u"]

result=""
for ch in text:

    if ch in vowels:

        result+=ch

re=set(result)
res=str(re)
print(res)