## Дополните приведенный код, используя индексатор, так чтобы он вывел 17-ый элемент списка `primes`.

```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])
```

## Дополните приведенный код, используя индексатор, так чтобы он вывел последний элемент списка `primes`.

```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])
```

## Дополните приведенный код, используя срезы, так чтобы он вывел первые 6 элементов списка `primes`.

> **Примечание.** Результатом вывода должна быть строка `[2, 3, 5, 7, 11, 13]`.****

```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[0:6])
```

## Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка `numbers`.

```python
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers)+min(numbers))
```

## Дополните приведенный код, так чтобы он вывел среднее арифметическое элементов списка `evens`.

```python
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens)/len(evens)
print(average)
```

## Дополните приведенный код, так чтобы элемент списка имеющий значение `Green` заменился на значений `Зеленый`, а элемент `Violet` на `Фиолетовый`. Далее необходимо вывести полученный список.

```python
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'

print(rainbow)
```

## Дополните приведенный код, так чтобы он вывел элементы списка `languages` в обратном порядке.

> **Примечание.** Для вывода списка воспользуйтесь функцией `print()`.

```python
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

print(languages[::-1])
```

## Дополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*), так чтобы он вывел список:

> `[1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]`.

```python
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1*2+numbers2*9+numbers3)
```


