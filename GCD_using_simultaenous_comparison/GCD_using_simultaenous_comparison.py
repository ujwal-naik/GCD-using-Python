def gcd(m,n):
    common_factor = []
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0 :
            common_factor.append(i)
    return(common_factor[-1])
n1= int(input("Enter the first number :"))
n2= int(input("Enter the second number :"))
result = gcd(n1,n2)
print (result)
    