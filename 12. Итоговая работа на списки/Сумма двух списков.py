s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = []
for i in range(len(s1)):
  s3.append(s1[i] + s2[i])
print(*s3)