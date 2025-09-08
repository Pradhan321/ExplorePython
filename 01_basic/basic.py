p1=[1,2,3]
print(p1)
# here the list is mutable but remember one thing when the p1 get reference like [1,2,3] and after this if you assign this p1 to new variable p2 then p2 directly point the reference of p1 and you change p1 then the changes also will reflect to p2 but you again assign another reference to the same variable p1 the p1 now point to another reference the changes that is happen in p1 will not be reflect to p2 variable 
p1=[1,2,3]
p1[1]=23
p2=p1
print(p2)

