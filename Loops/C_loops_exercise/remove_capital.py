def remove_capitals(text):
    for i in text:
        if i != i.upper():
            print(i, end="")
            
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'