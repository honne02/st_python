s, counter = input(), 0
for i in s:
    if i != i.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)