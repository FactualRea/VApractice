def max_object_value(dict):
    result = []
    max_num = 0
    for key, value in dict.items():
        for key2, value2 in dict.items():
            if value > value2:
                result = [key, value]
    return result

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]