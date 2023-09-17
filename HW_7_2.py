# Задание №3
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from Seminar_1 import my_func
from Seminar_2 import my_func as my_func2
from HW_7_1 import group

if __name__ == '__main__':
    my_func(10, 'file_1.jpg')
    my_func2(10, 'file_2.jpg') # функцию, которая генерирует псевдоимена.
    group(jpg=2, bin=4, png=8) # функцию которая генерирует файлы с разными расширениями
    


