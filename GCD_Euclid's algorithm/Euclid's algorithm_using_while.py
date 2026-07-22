def gcd(m,n):
    if   m<n:
        (m,n) = (n,m)
    while (m%n) != 0:
        diff = m - n
        (m,n) = (max(n,diff), min(n,diff))
    return n


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = gcd(n1, n2)
print("GCD is : ", result)
