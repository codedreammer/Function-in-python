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

#

def my_function(fname):
  print(fname + " Refsnes","AND send")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#The pass Statement

def myfunction():
  pass

