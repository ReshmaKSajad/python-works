def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(13))



def prime_or_not(n):
    if n==1:
        return False

    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
print(prime_or_not(9))


















