def modInverse(m):
    print("\n** We will find d with inverse mode operation **")
    a = int(input("Enter the value 'e' : "))
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x

def primeMultipliers(number):
    i = 2
    list = []
    multiplier = []

    while i < number:
        if number % i == 0:
            list.append(i)
        i += 1
    del i
    for i in list:
        finish  = True
        for a in list:
            if (finish ):
                if (i == a):
                    multiplier.append(i)
                elif (i % a == 0):
                    finish  = False
    return  multiplier

def multiplication(x,y):
    return (x-1)*(y-1)
