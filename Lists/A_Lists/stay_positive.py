def stay_positive(numbers):
    positive_numbers = []
    for num in numbers:
        if num >= 0:
            positive_numbers.append(num)
    print(positive_numbers)
    
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []