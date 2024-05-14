# how to know all the methods in a list
# write python,then dir(list)
# list methods =append,count(ob),index(ob),pop(),insert(index,obj),remove(obj),copy()

orders=["friedrice","biriyani","bb","cb","aa"]
#           0           1        2     3    4
#                                       -2    -1

# orders.append("tea")#only to last position
# print(orders)

# print(orders.count("cb"))

# print(orders.index("biriyani"))

print(orders.pop())
# print(orders)
# print(orders.pop(1))   #remove the obj in 1 index
# print(orders)

# print(orders.insert(2,"gheerice"))#doubt



orders.remove("cb")#the first occurence only remove
print(orders)
