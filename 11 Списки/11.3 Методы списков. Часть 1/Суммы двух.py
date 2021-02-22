n, a = int(input()), int(input())
lst = []
for _ in range(n-1):
    b = int(input())
    lst.append(a + b)
    a = b
print(lst)