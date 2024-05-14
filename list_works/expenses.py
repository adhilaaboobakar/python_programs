expenses =[12000,13000,23000,24000,25000,32000,23000]#this is list object

# print(len(expenses))

# for i in range(0,len(expenses)):
#     print(expenses[i])

# for exp in expenses:
#     print(exp)

# # print all expenses>20000
# for i in range(0,len(expenses)):
#     if expenses[i]>20000:
#         print(expenses[i])
# print the expenses bw 15k and 25k

for i in range(0,len(expenses)):
    if expenses[i] in range(15000,25000):
        print(expenses[i])

# max_exp= max(expenses)
# print(max_exp)

# min_exp= min(expenses)
# print(min(expenses))

# total expense
total_expenses=sum(expenses)
print(total_expenses)

# average expense
avg_exp=total_expenses/len(expenses)
print(avg_exp)

print(sorted(expenses,reverse=True))

