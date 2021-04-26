n = input().split()
for i in n:
    i1 = i[0]
    i = i[1:]
    i = i + i1 + 'ки'
    print(i, end = ' ')


'''
string = input().split()

for i, word in enumerate(string):
    string[i] = word[1:] + word[0] + 'ки'

print(*string)
'''