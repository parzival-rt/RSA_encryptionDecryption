#                              C = M^e mod n
# you must number type quadruple

e = int(input("Enter the value 'e' : "))
n = int(input("Enter the value 'n' : "))

kacDortluVar = int(input("Number of blocks with four : "))
i=0
answer=[]
while(i<kacDortluVar):
    dortlu = int(input("Enter the {}. quadruple block : ".format(i+1)))
    value = (dortlu**e)%n
    answer.append(value)
    i += 1

print("Encrypted text : ",*answer)