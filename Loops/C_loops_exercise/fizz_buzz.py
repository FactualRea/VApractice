def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            print(i)

fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3
# 5
# 6
# 9
# 10
# 12
# 18
# 20
# 21
# 24
# 25
# 27
# 33