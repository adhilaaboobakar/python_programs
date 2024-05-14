f=open("C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\news.txt","r")

# count=0
# for line in f:
#     words=line.rstrip("\n").split() #after splitting it appears as list
#     print(words)
#     # total number of words
#     count=count+len(words)

# print(count)


# word_count from the file news.txt


wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    print(words)
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1

print(wc)

