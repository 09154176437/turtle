number = 13
def is_prime(asghar):
    for i in range(2,asghar):
        if asghar % i == 0 :
            return False
    return True

print(is_prime(number))