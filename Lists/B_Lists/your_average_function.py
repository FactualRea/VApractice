def your_average_function(numbers):
    sum = 0
    for i in numbers:
        sum += i
    if len(numbers) == 0:
        print(None)
    print(sum / len(numbers))

your_average_function([5, 2, 7, 24]) #-> 9.5
your_average_function([100, 6]) #-> 53
your_average_function([31, 32, 40, 12, 33]) #-> 29.6
your_average_function([]) #-> None
