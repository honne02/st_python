## Установите соответствие между списочным методом и тем, что он выполняет.

### Сопоставьте значения из двух списков

| insert()      | вставляет заданное значение в список                         |
| :------------ | :----------------------------------------------------------- |
| **index()**   | **возвращает индекс первого вхождения заданного значения**   |
| **reverse()** | **меняет порядок следования элементов на противоположный**   |
| **count()**   | **возвращает количество равных заданному значению элементов**|
| **clear()**   | **удаляет все элементы из списка**                           |
| **find()**    | **у списков такой метод отсутствует 😂**                     |
| **remove()**  | **удаляет первое вхождение заданного значения**              |

## Что будет выведено в результате выполнения следующего программного кода?

```python
colors = ['Orange']
colors.append('Red')
colors.append('Blue')
colors.append('Green')
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')

print(colors)
```

```
['Violet', 'Orange', 'Purple', 'Red', 'Blue', 'Green']
```

##Что будет выведено в результате выполнения следующего программного кода?

```python
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
del colors[-1]
colors.remove('Green')

print(colors)
```

```
['Red', 'Blue', 'Black']
```

