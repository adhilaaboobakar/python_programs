# here we discuss some predefined characters
from re import *


text="ab CaK7@#"

# pattern="\d"#[0-9]
# pattern="\D" # exclude digit[^0-9]
# pattern="\w" #alphanumeric [a-zA-Z0-9]
pattern="\W" #exclude alphanumeric,only special characters


matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())