items=["bat","ball","cricketball","stumps","helmet","arc"]
# print longest word
# max= print with the alphabet wise max. if there is a word with z then print that word 

longest_word=max(items,key=lambda w:len(w))
print(longest_word)

smallest_word=min(items,key=lambda w:len(w))
print(smallest_word)

# # def get_len(w):
# #     return len(w)

# small= min(items,key=get_len)
# print(small)

# print total character sum in the items
count=0
for item in items:
    count=count+len(item)
print(count)
