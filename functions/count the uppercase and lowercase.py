def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


def string_test(s):
    d= {"UPPERCASE":0,"lowercase":0}
    for i in s:
        if i.isupper():
            d["UPPERCASE"]=d["UPPERCASE"]+1
        elif i.islower():
            d["lowercase"]=d["lowercase"]+1
    print("original string : ",s)
    print("number of uppercase letters =",d["UPPERCASE"])
    print("number of lowercase letters =",d["lowercase"])
string_test("My Ikka is Bennus")


def string_test(s):
    d={"UPPERCASE":0,"lowercase":0}
    for k in s:
        if k.isupper():
            d["UPPERCASE"]=d["UPPERCASE"]+1
        elif k.islower():
            d["lowercase"]=d["lowercase"]+1
    print("original string :",s)
    print("number of uppercase letters =",d["UPPERCASE"])
    print("number of lowercase letters =",d["lowercase"])
string_test("Reshma is a Good Girl")











