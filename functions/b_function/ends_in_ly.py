def ends_in_ly(word):
    if word[-1] == 'y' and word[-2] == 'l':
        return True
    else:
        return False

print(ends_in_ly("pretty"))      # False
print(ends_in_ly("instant"))     # False
print(ends_in_ly("analytic"))    # False
print(ends_in_ly("timidly"))     # True
print(ends_in_ly("fly"))         # True
print(ends_in_ly("gallantly"))   # True
