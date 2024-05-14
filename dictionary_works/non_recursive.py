text="ABCABBDE"
# print non repeating characters

nr={}

for ch in text:
    if ch in nr:
        nr[ch]+=1
    else:
        nr[ch]=1

for k,v in nr.items():
    if v==1:
        print(k)
