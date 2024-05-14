# input : ababcd
# output : abcd


# strings in python are immutable.it doesnt modify orginal string.it returns new string with the replacements.

def remove_dup(string):
    result=""
    for ch in string:
        if ch not in result:
            result+=ch
    return result

print(remove_dup("ababcd"))
 