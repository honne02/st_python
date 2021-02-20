# this is temp file
s = input()

out = ''
a,b = 0,0
i=0
while(i<len(s)):
  if(s[i] == 'h'):
    out += s[a:i+1]
    a = i
    b = (s[i+1:]).find('h')
    p = s[a: b+1]
    out += p[::-1]
    i = b+1
  else: out+=s[i]
  i+=1
print(out)