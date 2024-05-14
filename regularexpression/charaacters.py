from re import *

text="kaBczabc 9@7c"
# to find how many locations  a or c 


pattern="[ac]"


# [ac]=either a or c
# [a-e]=matching characters from a-e
#[a-z]
# [A-Z]=matches all uppercase alphabets
# [a-zA-Z]=matches all alphabets.no comma needed
# [0-9]=check for all digits
# alphanumeric characters[a-zA-Z0-9]


matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
