n = int(input("Enter a number: "))
for i in range(1,n):
  c = 0
  if n%i == 0:
    for j in range(1,i+1):
      if i%j == 0:
        c+=1
    if c==2:
      print(i)
