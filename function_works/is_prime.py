def prime_check(num):

    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    return is_prime
print(prime_check(9))