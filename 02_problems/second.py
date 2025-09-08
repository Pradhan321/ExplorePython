# check discount on age and days

person_age=int(input("Enter person age : "))
days=input("Enter week days : ")

price=12 if person_age>18 else 8
print("ordinary day : ",price)
if days=="wednesday":
  price-=2
  print("horahh! today is wednesday you get 20% off" ,price)