s = input()
if(s.find('f')==-1): print(-2)
elif(str(s[s.find('f')+1:]).find('f')!=-1): 
  print(str(s[s.find('f')+1:]).find('f')+s.find('f')+1)
else: print(-1)