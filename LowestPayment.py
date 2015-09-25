balance=10000
annualInterestRate=.08
lower=balance/12
tol=.000001
upper=(balance*(1+(annualInterestRate/12))**12)/12
payment = (lower+upper)/2
testbalance=balance
guesses=0
while testbalance>tol or testbalance<(-tol):
    testbalance=balance
    payment=(lower+upper)/2
    for x in range(0,12):
        testbalance=testbalance-payment
        testbalance=testbalance*(annualInterestRate/12)+testbalance
    if testbalance>0:
        lower=payment
    elif testbalance<0:
        upper=payment
    guesses+=1
print guesses
print('Lowest Payment: ' + str(payment))