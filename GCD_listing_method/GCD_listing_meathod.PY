def gcd(m,n):
    factor_m =[]
    for i in range(1,m+1):
        if (m%i)== 0:
            factor_m.append(i)  

    factor_n  =[]
    for j in range(1,n+1):
        if (n%j)== 0:
            factor_n.append(j)

    common_factor=[]
    for f in  factor_m:
        if f in factor_n:
            common_factor.append(f)

    return common_factor[-1]

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = gcd(n1, n2)
print ("GCD is : ",result)