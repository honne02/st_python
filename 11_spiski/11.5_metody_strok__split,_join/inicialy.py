s = input()
s1 = s.split()
t = []
for w in s1:
    t.append(w[0])
print('.'.join(t),'.', sep = '')