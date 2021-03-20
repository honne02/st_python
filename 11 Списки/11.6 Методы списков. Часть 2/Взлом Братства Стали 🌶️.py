n = int(input())
for _ in range(n):
  a = input()
  if('#' in a): print(a[:a.count('#')].rstrip())
  else: print(a.rstrip())