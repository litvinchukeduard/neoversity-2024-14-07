# python3 read_file.py '/Моя папка/' 
# python3 read_file.py /Моя\ папка/
# python3 read_file.py \"file\".txt

# 1) Отримати аргумент з терміналу

# 2) Відкрити файл та прочитати все що є всередині

# 3) Вивести все це у термінал

import sys
'''
Написати додаток, який буде читати шлях до файлу та виводити те що є у файлі у термінал
'''

# 2) 
def read_file_contents(file_path: str) -> str:
    # file = open(file_path)

    # file.close()

    with open(file_path) as file:
        return file.read()
    # with open(file_path) as file:
    #     # for line in file.readlines(): Читає увесь файл
    #     for line in file: # Читає лише перший рядок
    #         print(line)


# 1) 

# 3)
# print(read_file_contents('"file".txt'))

# print(sys.argv)
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    print(read_file_contents(file_path))
else:
    print('Error: please provide file path')
