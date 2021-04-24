st = input()
first = st.find('h')
last = st.rfind('h')
st = st[:first] + st[(last + 1):]
print(st)