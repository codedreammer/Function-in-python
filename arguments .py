#def average(a = 9, b=1):
 #   print("The average iss",(a+b)/2)


#average()
#def name(fname, mname = "jhon",lname = "whatson"):
 #   print("hello",fname,mname,lname)
#
#name("amy","agarwal","jain")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i 
        print("Average is:",sum/len(numbers))
    
    average(5, 6, 7, 1)


