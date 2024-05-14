arr=[4,9,5,6,9,5,4,7]

# find duplicate numbers
arr.sort()
print(arr)

current_word=arr[0]

i=0
j=1
for i in range(0,len(arr)):
    for j in range(1,len(arr)+1):
      current_num=arr[i]
      nxt_num=arr[j]
      if current_num-nxt_num==0:
         print(current_num)

     



































# arr.sort()

# i=0
# while(i<len(arr)-1):
#     j=i+1
#     ith_element=arr[i]
#     jth_element=arr[j]

#     diff=jth_element-ith_element
#     if diff==0:
#         print(ith_element)
#         i=j
#     i+=1
    



