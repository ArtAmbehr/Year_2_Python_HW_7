# Задание №2 
# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os

def group_rename_files(dest_name, num_digits, src_ext, dest_ext, name_range=None):
    
    files = os.listdir()    
    files = [f for f in files if os.path.isfile(f) and f.endswith(src_ext)]

    if name_range:
        files = [f[name_range[0] - 1:name_range[1]] for f in files]

    count = 1
    
    for file in files:
        
        new_file_name = dest_name + str(count).zfill(num_digits) + dest_ext
        os.rename(file, new_file_name)
        count += 1

group_rename_files("new_file_", 4, ".txt", ".jpg", [3, 6])