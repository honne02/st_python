dat = []
for _ in range(int(input())):
    el = input()
    if el not in dat:
        dat.append(el)
        print(el)