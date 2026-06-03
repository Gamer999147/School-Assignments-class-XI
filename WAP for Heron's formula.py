import math #inputting the module
side1=int(input('Enter the value of side 1 '))
side2=int(input('Enter the value of side 2 '))
side3=int(input('Enter the value of side 3 '))
          
s=(side1+side2+side3)/2

h=(s*(s-side1)*(s-side2)*(s-side3))

print(math.sqrt(h))





