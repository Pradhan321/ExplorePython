number=int(input("Enter a number"))

count_even=0

for i in range(1,number+1):
  if(i%2==0):
    count_even+=1

print("Sum of even number is : ",count_even)
