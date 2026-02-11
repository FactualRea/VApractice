def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(11))# True
print(is_prime(8))# False
print(is_prime(7))# True
print(is_prime(21))# False
print(is_prime(2))# True
print(is_prime(15))# False
print(is_prime(1))# False
