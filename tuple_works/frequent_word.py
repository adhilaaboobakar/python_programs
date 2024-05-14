word="pneumonoultramicroscopicsilicovolcanoconiosis"
# find most frequent character

word_lst=[ ch for ch in word]

max=word_lst[0]

for ch in word_lst:
    value=word_lst.count(ch)
print(max)

    