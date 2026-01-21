def reverse_iterate(text):
    for i in range(len(text)-1, -1, -1):
        print(text[i])

reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b