def parity(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

print(parity(5))       # "odd"
print(parity(7))       # "odd"
print(parity(13))      # "odd"
print(parity(32))      # "even"
print(parity(10))      # "even"
print(parity(602348))  # "even"
