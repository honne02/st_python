s = input()
max_n, max_s = 0, ""
for i in s:
  if(s.count(i)>=max_n):
    max_n = s.count(i)
    max_s = i
print(max_s)