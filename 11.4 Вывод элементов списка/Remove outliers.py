s, x = [], int(input())
for i in range(x):
    s.append(int(input()))  
del s[s.index(min(s))]
del s[s.index(max(s))]
print(*s, sep= '\n')