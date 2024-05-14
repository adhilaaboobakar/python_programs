
from re import* #(finditer(),fullmatch(),search())

text="fat-cat-fast-catcher"
pattern="at"

matcher=finditer(pattern,text)#[(start,group),(start,group)]
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)
