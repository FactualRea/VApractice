def total(numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(total)

total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0