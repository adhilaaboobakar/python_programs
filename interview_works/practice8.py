# reverse words in a given string


# o/p : "meow cat speak cow"




text="cow speak cat meow"

s=text.split()[::-1]
l=[]
for item in s:
    l.append(item)
    st=("".join(l))
print(st)

