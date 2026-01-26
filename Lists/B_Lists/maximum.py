def maximum(numbers):
    max_num = 0
    for num in numbers:
        if len(numbers) == 0:
            return None
        if max_num < num:
            max_num = num
    print(max_num)



maximum([5, 6, 3, 7])
maximum([17, 15, 19, 11, 2])
maximum([])