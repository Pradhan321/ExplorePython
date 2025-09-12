def first_value(num):
  def second_value(x):
    return x**num
  return second_value

f=first_value(2)
g=first_value(3)

print(f(2))
print(g(2))