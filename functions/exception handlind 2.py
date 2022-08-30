try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a/b
    print(c)
#except ZeroDivisionError:
#    print("not enter zero as second number")
#except ValueError:
#    print("you must enter a number")
except (ValueError,ZeroDivisionError):
    print("you must enter a number other than zero")
except:
    print("all other errors handle error")
else:               #execute if there is no errors
    print("there is no errors")
finally:            #it always execute if there is an error or not
    print("always execute")