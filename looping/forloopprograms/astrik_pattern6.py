# O
# O E
# O E O
# O E O E 
# O E O E O  

for row in range(1,6):
    for coloumn in range(1,row+1):
        print("O" if coloumn%2!=0 else "E", end=" ")
    print()
