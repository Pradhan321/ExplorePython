fruit=input("Enter a fruit name : ")

fruit_color=input("tell me the color of the fruit based on the color i will tell you the condition of the fruit : ")

if fruit_color=="Green":
  condition="Unripe"
  print(fruit, "is fresh but not ready for eat")
  print(condition)

elif fruit_color=="yellow":
  print(fruit, "is fresh, we can enjoy the fruit")
  condition="ripe"
  print(condition)

else:
  print(fruit, "is not good, it is not eateble")
  condition="Overripe"
  print(condition)