"""Задание 2 ДЗ 1"""
import os


def str_list_to_lower(lst):
    """
    Преобразует все строки в списке к нижнему регистру.
    """
    return [el.lower() for el in lst]


def is_keywords_in_line(keywords, line):
    """
    Проверяет, содержатся ли ключевые слова в строке.
    """
    if any(keyword in line for keyword in keywords):
        return True
    return False


def filter_lines_by_keywords(file, keywords):
    """
    Фильтрует строки файла на основе ключевых слов.

    Открывает файл по указанному пути или использует переданный файловый объект.
    Затем проверяет каждую строку файла на наличие ключевых слов, и возвращает
    строки, в которых хотя бы одно ключевое слово содержится.
    """
    if isinstance(file, str):
        if not os.path.exists(file):
            raise FileNotFoundError(f"Файл '{file}' не найден")
        opened_file = open(file, 'r', encoding='utf-8')
    else:
        opened_file = file

    keywords_lower = str_list_to_lower(keywords)

    for line in opened_file:
        line = line.strip()
        lower_line = str_list_to_lower(line.split())
        if is_keywords_in_line(keywords_lower, lower_line):
            yield line

    opened_file.close()
