# Задание 2.
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
from string import ascii_lowercase

vowels = set('euioa')
consonants = set(ascii_lowercase).difference(vowels)
def random_name():
    len_name = random.randint(4, 7)
    name = ''
    for i in range(len_name):
        name += random.choice(list(vowels)) if i % 2 else random.choice(list(consonants))
    return name.title()


for _ in range(10):
    print(random_name())