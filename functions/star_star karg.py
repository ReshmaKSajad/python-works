#**kargs - it is variable length arguement along with keyword arguement
#type = dictionary
def fun(**karg):
    #print(type(karg))
    for k,v in karg.items():
        print(k,":",v)
fun(name = "RESHMA",department = "BCA")