a = input().split(" ")
for i in range(len(a)):
  a[i] = a[i].lower()
print('Общее количество артиклей:',a.count('an') + a.count('a') + a.count('the'))