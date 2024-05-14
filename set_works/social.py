
# print the suggestions to mohanlal in instagram
insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}

mohanlal_followings={"prithvi","vijay","lalu"}

dq_friends={"prithvi","fahad","sureshgopi","lalu"}



suggestions_mohanlal=insta_users.difference(mohanlal_followings)
suggestions_mohanlal.discard("mohanlal")
print(suggestions_mohanlal)

# find mutual friends in dq and mohanlal

mutual_frnds=mohanlal_followings.intersection(dq_friends)
print(mutual_frnds)

order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}

order2={"cb","friedrice","nan","upuma","vegmeals","idly"}

# create an order 3 in that either elements in set1 or set2 not in both

union_set=order1.union(order2)
inter_section=order1.intersection(order2)
new_order=union_set.difference(inter_section)

print(new_order)

# set1 U set2 - set1 intersection set2 ==this is called symmetric difference
# already inbuilt method there

new_order=order1.symmetric_difference(order2)
print(new_order)

# update one set with another set

st1={10,20,30}
st2={100,200,300}

st1.update(st2)
print(st1)



