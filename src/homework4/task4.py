"""
Даны два списка чисел. Посчитайте, сколько различных
чисел входит только в один из этих списков
"""

lst1 = [1, 2, 3, 6]
lst2 = [3, 6, 8, 9]
set_ = set(lst2) - set(lst1)
print(len(set_), set_)
