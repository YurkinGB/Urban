#Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {'Ali': 1989, 'Sultan' : 1990, 'Ivan' : 1987, 'Pavel' : 2003 }

#Выведите на экран словарь my_dict.
print('Выведите на экран словарь my_dict')
print(my_dict)

print('____________________________________________________________________________________________________________')

#Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print('Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.')
print(my_dict['Sultan'])
print(my_dict.get('Sveta'))

print('____________________________________________________________________________________________________________')

#Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Irina' : 1999, 'Stas' : 1965})

#Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
print('Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.')
print(my_dict.pop('Ali'))

#Выведите на экран словарь my_dict.
print('Выведите на экран словарь my_dict.')
print(my_dict)

print('____________________________________________________________________________________________________________')

#Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 2, 3, 3, 'Igor', (55, 66, 96), False, True, False}

#Выведите на экран множество my_set (должны отобразиться только уникальные значения)
print('Выведите на экран множество my_set (должны отобразиться только уникальные значения)')
print(my_set)

#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(4)
my_set.add('Sveta')

#Удалите один любой элемент из множества my_set.
my_set.discard(2)

#Выведите на экран измененное множество my_set.
print('Выведите на экран измененное множество my_set.')
print(my_set)