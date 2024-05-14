text="ABCABDE"

wc={}
dup_cha=[]

for ch in text:
    if ch not in wc:
        wc[ch]=1
    else:
        wc[ch]+=1
        dup_cha.append(ch)
print(dup_cha[1])