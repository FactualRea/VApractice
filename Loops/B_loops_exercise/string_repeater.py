def string_repeater(text, n):
    for i in range(n):
        print(text, end="")

string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3)



def string_repeater(text, num):
    ans_str = ""
    for i in range(num):
        ans_str += text
    print(ans_str)

string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo' 
string_repeater("tac", 3)