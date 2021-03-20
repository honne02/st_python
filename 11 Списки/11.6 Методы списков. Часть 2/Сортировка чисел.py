a = list(map(int, input().split()))
a.sort()
print(*a)
print(*a[::-1])