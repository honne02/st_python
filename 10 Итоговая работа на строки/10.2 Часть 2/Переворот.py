s = input()
print(s[0:s.find('h') + 1] + str(s[s.find('h') + 1:s.rfind('h')])[::-1] + s[s.rfind('h'):])