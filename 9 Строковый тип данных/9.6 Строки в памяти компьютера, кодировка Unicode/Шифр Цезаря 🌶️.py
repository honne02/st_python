n = int(input())
for i in input():
  if (ord(i)-n)<97:
    print(chr(122-(n-(ord(i)-96))), end='')
  else:
    print(chr(ord(i)-n), end='')

#n = int(input())
#[print(chr(122-(n-(ord(i)-96))) if (ord(i)-n)<97 else chr(ord(i)-n), end='') for i in input()]