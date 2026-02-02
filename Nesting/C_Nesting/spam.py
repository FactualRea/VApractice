def spam(pairs):
    str = []
    for p in pairs:
        w = p[0]
        n = p[1]
        for i in range(n):
            str.append(w)
    return " ".join(str)

array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'
