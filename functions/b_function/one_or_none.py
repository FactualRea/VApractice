def one_or_none(v1, v2):
    if v1 == v2:
        return False
    else:
        return True

print(one_or_none(False, False))   # False
print(one_or_none(True, False))    # True
print(one_or_none(False, True))    # True
print(one_or_none(True, True))     # False