number=int(input("Enter a number : "))



for j in range(2,number+1):
    is_prime=True
    for i in range(2,j):
      if(j%i)==0:
        is_prime=False
        break
    if is_prime:
      print(j)
   