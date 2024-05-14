
# return the smallest number from 2 numbers

def sm_num(n1,n2):
    res=n2 if n1>n2 else n1 
    return res
print(sm_num(2,1))

# n1=432,n2=45 return n1 return the smsllest digit in oneth plsce

def oneth_dig(n1,n2):
    last_n1 = n1%10
    last_n2=n2%10
    res=n1 if last_n1<last_n2 else n2
    return res
print(oneth_dig(432,18))
    

