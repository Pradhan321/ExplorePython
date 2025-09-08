# Age group catagorize 

person_age=int(input("Enter you age then i will tell you that you belong to which catogory : "))
if person_age<13:
  print("Child")             

elif person_age>13 and person_age<19:
  print("Teenager")

elif person_age>19 and person_age<60:
  print("Adult")

else:
                             
  print("Senior")