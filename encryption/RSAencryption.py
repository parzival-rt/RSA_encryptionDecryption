#                              C = M^e mod n
# you must number type quadruple

e = int(input("Enter the value 'e' : "))
n = int(input("Enter the value 'n' : "))

numberQuadruple = int(input("Number of blocks with four : "))
i=0
answer=[]
while(i<numberQuadruple):
    Quadruple = int(input("Enter the {}. quadruple block : ".format(i+1)))
    value = (Quadruple**e)%n
    answer.append(value)
    i += 1

print("Encrypted text : ",*answer)
