def gcd(m,n):
    if m < n:
        (m, n) = (n, m)
        
    if (m%n) == 0:
        return n
    else:
        diff = m - n
        return gcd(max(n, diff), min(n, diff))

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = gcd(n1, n2)
print ("GCD is : ",result)