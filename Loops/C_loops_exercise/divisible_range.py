def divisible_range(min, max, num):
    for i in range(min, max):
        if i % num == 0:
            print(i)


# Example:
divisible_range(17, 40, 9)
# 18
# 27
# 36

divisible_range(10, 24, 4)
# 12
# 16
# 20