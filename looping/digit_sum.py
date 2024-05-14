num=123
sum=0
# first_find sum= digit-sum
# find 1**3+2**3+3**3= pre-arm

while(num!=0):
    digit=num%10
    digit_cube=digit**3
    sum+=digit_cube
    num=num//10

print(f"sum is {sum}")