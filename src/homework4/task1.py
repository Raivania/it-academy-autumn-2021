""""
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
"""

dct_ = {el: el**2 for el in range(21)}
print(dct_)
