def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


a = 9 
b = 8
if(a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")

    
c = 12
d = 10
if(c<d):
    print("first number is smaller")
else:
    print("number is smaller then the first")

c = 8
d = 74
isGreater(c, d)
calculateGmean(c,d)
