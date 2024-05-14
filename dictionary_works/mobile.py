mobile={"id":100,"name":"Iphone","price":100000,"imei":2345,"processor":"apple"}

# print all key value pairs

for k,v in mobile.items():
    print(k,v)

# print name

print(mobile.get("name"))   # or print(mobile["name"])


# print price
print(mobile.get("price"))

# update price as rs 85000

mobile.update({"price":85000})  #or mobile["price"]=85000  print(mobile)
print(mobile)   

# remove imei

mobile.pop("imei")
print(mobile)

# add one item offers key to the dicttionary

mobile.update({"offer" :1000}) #or mobile["offer"] = 1000
print(mobile)

# 1000 rs amount added to price

mobile["price"]+=1000
print(mobile)

# to check color is there in dictionary

print("color" in mobile)

