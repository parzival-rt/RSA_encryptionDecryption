from functionss import *

n = int(input(("Enter the value 'n' : ")))

primes = primeMultipliers(n)
x = primes[0]
y = primes[1]
print("X : {} , Y : {}".format(primes[0],primes[1]))
print("{} * {} = {} ".format(x-1,y-1,multiplication(x,y)))

d = modInverse(multiplication(x,y))
print("m : ",multiplication(x,y))
print("d : ",d)

dortluSayisi = int(input("\nNumber of blocks with four : "))

answers=[]
z=0
while(z<dortluSayisi):
    value = int(input("Enter the {}. quadruple block : ".format(z+1)))
    answers.append((value**d)%n)
    z+=1
print(*answers)





