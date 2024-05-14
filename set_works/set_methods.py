# set methods
# for adding add()method used,we can't predict the index, in list by append method for adding elements
#add,union,intersection,difference,pop,remove,discard 
#           mutualelements


# diff b/w remove and discard = if we use remove,the object is not there,it return error and the program stopped without executing the remaining steps
# but in discard no error,if the object is not there ,it doesnt removes,remaining pgm will execute


# colors={"red","green","blue"}
# # add
# colors.add("yellow")
# print(colors)


# intersection() method
st1={"red","blue","black"}
st2={"purple","cyan","blue","yellow"}

inter_set=st1.intersection(st2)
print(inter_set)

# union method()
union_set=st1.union(st2)
print(union_set)

# difference() method    , delete the elements from set1 that is common to set 2 and the remaining elements of set1 are print
diff_set=st1.difference(st2)
print(diff_set)

# # remove one element   ,the first element should be removed from their order
# st1.pop()
# print(st1)

# # remove the specific object
# st1.remove("black")
# print(st1)

# 
st1.discard("blue")