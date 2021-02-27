s = list(map(int, input().split()))
k = 0
for i in range(len(s)-1):
  for u in range(i+1,len(s)):
    if s[i]==s[u]: k+=1
print(k)