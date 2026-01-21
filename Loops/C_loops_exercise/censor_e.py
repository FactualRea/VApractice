def censor_e(text):
    cens = ""
    for i in text:
        if i == "e":
            cens += "x"
        else:
            cens += i
    print(cens)
    
censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'
