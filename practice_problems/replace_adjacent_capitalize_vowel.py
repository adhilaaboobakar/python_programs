# replace everyb letter by adjacent letter
# capitalize vowels
# no change in special character


def new_string(string):
    result=""
    for ch in string:
        if ch.isalpha():
            new_ch=chr(ord(ch)+1)
            if new_ch in "aeiou":
                new_ch=new_ch.upper()
            else:
                new_ch=new_ch.lower()
            if ch.islower() and new_ch > 'z':
                new_ch = 'a'.upper()
        else:
            new_ch=ch
        result+=new_ch
    return result

print(new_string("acfgent**dz"))