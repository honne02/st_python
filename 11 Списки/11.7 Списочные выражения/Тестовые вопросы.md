## Как записывается списочное выражение?

### Выберите один вариант из списка

* [выражение for переменная in последовательность]
* [выражение for последовательность in переменная]
* [переменная for выражение in последовательность]
* [переменная for переменная in выражение]

```
[выражение for переменная in последовательность]
```

## Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.

```python
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [i[1:] for i in keywords]

print(new_keywords)
```

## Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.

```python
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(i) for i in keywords]

print(lengths)
```

## Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).

```python
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [i for i in keywords if len(i)>=5]

print(new_keywords)
```

## Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от 100 до 1000.

```python
palindromes = [i for i in range(100, 1000) if str(i)[::-1]==str(i)]

print(palindromes)
```