s = input()
for i in range(len(s)):
    if s[i] == ' ':
        break
s1,s2 = s[:i],s[i+1:]
if s1[0] == s1.title()[0] and s2[0] == s2.title()[0]:
    print('YES')
else:
    print('NO')