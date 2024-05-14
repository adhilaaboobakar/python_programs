
# Find the length of sequence with maximum number of zeoros.



data_list = [1, 0, 8, 0, 0, 4, 5, 0, 0 , 0, 0,0]

curr_len=0
max_len=0

for num in data_list:

    if num==0:
        curr_len+=1
        
        if curr_len>max_len:
            max_len=curr_len

    else:
        curr_len=0


print(max_len)



