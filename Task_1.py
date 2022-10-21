# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Примечание Текст находится в файле. Его надо считать, текст исправить, 
# исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста


# Получение данных из файла
def read_file(file) -> str:
    with open(str(file), 'r', -1, 'utf-8') as data:
        file = data.read()
    return file


# Записать данные в файл
def write_to_file(data: str, filename: str) -> None:
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(data)


# Удаляет слова с указанными символами
def del_words_char(file_orig: str, symbol: str) -> str:
    file_orig = list(filter(lambda x: symbol not in x, file_orig.split()))
    return " ".join(file_orig)


file_orig = read_file('Homework\Homework-5\original_text.txt')
file_cor = del_words_char(file_orig, 'абв')
write_to_file(file_cor, 'Homework\Homework-5\corrected_text.txt')
# print(file_orig) # посмотреть в консоли
# print(file_cor) # посмотреть в консоли


