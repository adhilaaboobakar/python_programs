
from re import* #(finditer(),fullmatch(),search())

text="aaabcaa9bacdaabd999"
# pattern="a*" #any number of a including zero
# pattern="[a-z]*" #any number including zeroes 
# pattern="[0-9]*"

pattern="a{2}" #it checks for exact 2a
# pattern="[0-9]{10}"


matcher=finditer(pattern,text)#[(start,group),(start,group)]

for m in matcher:
    print(m.start(),m.group())


