previous_num=0
current_num=1
# print(previous_num, end=",")
# print(current_num , end=",")


print(f"{previous_num},{current_num}",end=",")
for i in range(1,11):
    next=previous_num+current_num
    print(next ,end=",")
    previous_num=current_num
    current_num=next




# # print("" end="\n")
# # to print good morning
# print("good", end= " ")
# print("morning", end="")
