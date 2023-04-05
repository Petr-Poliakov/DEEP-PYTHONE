"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os


def rename_files(directory, desired_name, num_digits, source_extension, target_extension):
    """
    Функция принимает переименновывает файлы в директории

    Функция принимает следующие аргументы:
      directory (str): директория (путь) в которой хранятся файлы
      desired_name (str): желаемое имя файла
      num_digits (int): количество знаков в порядкомов номере
      source_extension (str): старое расширение файла
      target_extension (str): новое расширение файла
    """
    files = os.listdir(directory)
    print(files)
    count = 1
    for file in files:
        if file.endswith(source_extension):
            filename = os.path.splitext(file)[0]
            # filename = filename[3:6]
            new_filename = f"{desired_name}_{str(count).zfill(num_digits)}.{target_extension}"
            count += 1
            os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))


rename_files("/Users/petrpolakov/Documents/Deep Python/venv/lesson7/DZ7", "new_tsk", 3, ".doc", "txt")

# def func (name_old: str, name_new: str):
#     for count, filename in enumerate(os.listdir(p)):
#         dst = f"{name_new} {str(count)}.py"
#         src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
#         dst = f"{folder}/{dst}"
#
#         # rename() function will
#         # rename all the files
#         os.rename(src, dst)
#
#
# func(file.txt, tsk.py)
#
#
# def func_rename_files (new_name: str, old_exp: str): #count_file: int, , new_exp: str
#     global list_dir
#     for obj in p:
#         if item in list_dir(old_exp):
#             p = Path(item)
#             p.rename(new_name)
#         print(item)

# func_rename_files(tsk, txt)

    # p = Path(Path().cwd())
    # count_file = int(0)
#     for obj in p.iterdir():
#         p = Path('name_f')
#         p.rename('new_name''count_file''exp_final_file')

# func_rename_files('task',2,'txt','py')

