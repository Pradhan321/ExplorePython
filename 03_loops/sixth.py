number=int(input("Enter a number : "))
factorial=1
while(number>0):
  factorial=number*factorial
  number-=1

print("factorial of a number is : ",factorial)
