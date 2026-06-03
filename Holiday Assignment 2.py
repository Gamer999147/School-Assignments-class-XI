import math
principle=int(input('Enter the principle '))
rate=int(input('Enter the rate '))
time=int(input('Enter the time '))
n=int(input('Enter the number of times interes is compounded '))
SI=int((principle*rate*time)/100)
print('The S.I. is ',SI)
m=int(principle*(1+(rate/100)/n)**(n*time))
print(m)

M=m-principle
print('The C.I. is ',M)
