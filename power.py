def power(base,exp):
    if(exp==0):
        return(base)
    if(exp!=0):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
