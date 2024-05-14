names=["rahul","manoj","raju","amal","eby"]

# print the names whose starting with vowels

# star_vow_name=[]
# for name in names:
#     if name[0] in ["a","e","i","o","u"]:
#         print(name)
# this is what like list comprehensioon
star_vow_name=[ name for name in names if name[0] in ["a","e","i","o","u"]]
print(star_vow_name)

# print the names whose starts with consonants

star_cons_name=[ name for name in names if name[0] not in ["a","e","i","o","u"]]
print(star_cons_name)