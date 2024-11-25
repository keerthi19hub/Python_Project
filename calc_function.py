def sum(a,b):
  return(a+b)

def sub(a,b):
  return(a-b)

def product(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

def factor(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
    
def abc(n):
    if n>1:
        for i in range(2,n):
            if n%2==0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")
        
        
                