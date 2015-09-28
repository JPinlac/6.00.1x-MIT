def primesList(N):
    if N>2:
        primes=[2,3]
    if N==2:
        primes=[2]
    for i in range(4,N+1):
        isprime=True
        for j in range(2,i):
            if i!=j:
                if i%j==0:
                    isprime=False
                    break
        if isprime==True:
            primes.append(i)
            
    return primes
