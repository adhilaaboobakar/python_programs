


# convert a string, comprising letters, digits, and symbols, into a valid mobile number by removing all non-digit characters, 
# and ensuring that if the resulting number exceeds 10 digits, it is trimmed down to 10 digits



def clean_num(input_str):

    res="".join(filter(str.isdigit,input_str))

    if len(res)>10:
        res=res[:10]


    return res

print(clean_num("2345#fgthk89u7998907"))