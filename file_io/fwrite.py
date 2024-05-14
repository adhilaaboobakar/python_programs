path= "C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\colors.txt"

# f=open(path,"w")

# f.write("hello") #only string should be added.


f=open(path,"w")
colors=["red","green","blue"]

for c in colors:
    f.write(c+"\n")