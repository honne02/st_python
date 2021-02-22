a = [int(input()) for i in range(int(input()))]
b, c = [], []
for i in a:
  if i < 0: print(i)
  elif i==0: b.append(i) 
  else: c.append(i)
print(*b+c, sep='\n')