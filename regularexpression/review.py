from re import *


text="akc7 @Kbc"

pattern="[^a-z]"# ^ implies it excludes the characters a-z here

# pattern="[^a-zA-Z0-9]"  : it takes special characters

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())