s = [input() for i in range(int(input()))]
d = [input() for i in range(int(input()))]
for i in s:
    for j in d:
        if j.lower() not in i.lower():
            break
    else:
        print(i)