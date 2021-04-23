a = input().split()
print('+'.join(a), end="=")
print(sum([int(i) for i in a]))