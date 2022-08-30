test = "aachi"
def check_scope():
    def do_local():
        test="reshma updated ***local test"
    def do_non_local():
        nonlocal test
        test="non local test"
    def do_global():
        global test
        test="global test"

    test="default"
    do_local()
    print("test value after do local:",test)
    do_non_local()
    print("test value after non do local:",test)
    do_global()
    print("test value after do global:",test)

print(test)
check_scope()
print("test value after main:",test)

