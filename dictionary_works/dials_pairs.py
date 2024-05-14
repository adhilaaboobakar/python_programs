# 1=[a,b,c]
# 2=[d,e,f]
# 3=[g,h,i]


# 12=(a,d)(a,e)(a,f)(b,d)(b,e)(b,f)(c,d)(c,e)(c,f)

dials={
    "1":["a","b","c"],
    "2": ["d","e","f"],
    "3": ["g","h","i"]
}


user_input="3"

main_lst=[]
for ch in user_input:
    sub_lst=dials.get(ch)
    main_lst.append(sub_lst)

pairs=[(i,j) for i in main_lst[0] for j in main_lst[1]]
print(pairs)


