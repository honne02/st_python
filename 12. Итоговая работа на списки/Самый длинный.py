s = input().split()
l = []

for i in s:
    l.append(len(i))

longest = max(l)

print(longest)
# print(max([len(i) for i in input().split()]))