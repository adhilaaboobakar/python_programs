
product={"code":1001,"name":"orange","price":35}

# for all keys =use key() method
for k in product.keys():
    print(k)

# for all values= use values() method
for v in product.values():
    print(v)

# for all keys and values= items() method
for k,v in product.items():
    print(k,v)


# update()
product.update({"name":"oranges"})
print(product)

# # delete specified element
product.pop("name")
print(product)

# # delete one item
# product.popitem()
# print(product)

# for deleting all items
# product.clear()
# print(product)


# # copy all items in the dictionary
# product.copy()
# print(product)


# product.get("name") =diff b/w get and bytaking direct
# print(product)



