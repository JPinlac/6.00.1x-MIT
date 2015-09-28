def count7(N):
    '''
    N: a non-negative integer

    Hint: Mod (%) by 10 gives you the rightmost digit 
    (126 % 10 is 6), while doing integer division by 10 
    removes the rightmost digit (126 / 10 is 12).
    '''
    if N==0:
        return 0
    if N%10==7:
        return 1+count7(N/10)
    return count7(N/10)
print count7(717)