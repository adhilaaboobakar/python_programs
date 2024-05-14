# 1
# 1 2
# 1 2 3
# 1 2 3 4

for row in range(1,5):
    for coloumn in range(1,row+1):
        print(coloumn, end="\t ")
    print()