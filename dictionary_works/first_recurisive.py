text="ABCABBDE"

# print first recursive character

rc={}

for ch in text:
    if ch not in rc:
        rc[ch]=1
    else:
        print(f"{ch} is first recursive character")
        break


