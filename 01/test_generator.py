"""Тесты к заданию 2 ДЗ 1"""
import unittest
from unittest import mock
import os
from generator import (filter_lines_by_keywords,
                       str_list_to_lower, is_keywords_in_line)


class TestTask(unittest.TestCase):
    """
    Набор тестов для функций модуля generator.
    """

    def setUp(self):
        """
        Выполняется перед каждым тестовым методом.
        """
        print("setUp")

    def tearDown(self):
        """
        Выполняется после каждого тестового метода.
        """
        print("tearDown")

    def test_str_list_to_lower(self):
        """
        Проверяет, что функция str_list_to_lower корректно
        переводит строки в нижний регистр.
        """
        test_string = "А розА уПАла На ЛаПу азоРА".split()
        self.assertEqual(str_list_to_lower(test_string),
                         ["а", "роза", "упала", "на", "лапу", "азора"])
        self.assertEqual(test_string, "А розА уПАла На ЛаПу азоРА".split())

    def test_is_keywords_in_line_true(self):
        """
        Проверяет, что функция is_keywords_in_line корректно
        определяет наличие ключевых слов в строке.
        """
        keywords = ["роза", "азора"]
        line = "а роза упала на лапу азора"

        self.assertEqual(is_keywords_in_line(keywords, line), True)
        self.assertEqual(keywords, ["роза", "азора"])
        self.assertEqual(line, "а роза упала на лапу азора")

    def test_is_keywords_in_line_false(self):
        """
        Проверяет, что функция is_keywords_in_line
        корректно определяет отсутствие ключевых слов в строке.
        """
        keywords = ["автобус", "энергетиков"]
        line = "а роза упала на лапу азора"

        self.assertEqual(is_keywords_in_line(keywords, line), False)
        self.assertEqual(keywords, ["автобус", "энергетиков"])
        self.assertEqual(line, "а роза упала на лапу азора")

    def test_is_keywords_in_line_zero_keywords(self):
        """
        Проверяет, что функция is_keywords_in_line
        корректно работает при пустом списке ключевых слов.
        """
        keywords = []
        line = "а роза упала на лапу азора"

        self.assertEqual(is_keywords_in_line(keywords, line), False)
        self.assertEqual(keywords, [])
        self.assertEqual(line, "а роза упала на лапу азора")

    def test_is_keywords_in_line_empty_line(self):
        """
        Проверяет, что функция is_keywords_in_line
        корректно работает при пустой строке.
        """
        keywords = ["роза", "азора"]
        line = ""

        self.assertEqual(is_keywords_in_line(keywords, line), False)
        self.assertEqual(keywords, ["роза", "азора"])
        self.assertEqual(line, "")

    def test_filter_lines_by_keywords_one_result(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        корректно фильтрует строки файла по ключевым словам.
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза'])]

        keywords = ["Роза"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_many_results(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        корректно фильтрует строки файла по ключевым словам,
        если по слову фильтру есть несколько совпадений.
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза',
                   'Роза цветок'])]

        keywords = ["Роза"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора", 'Роза цветок']

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_all_result(self):
        """
        Если все строки файла подходят
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Роза цветок', 'а роза'])]

        keywords = ["РозА"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора", "Роза цветок", "а роза"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_case_insensitive(self):
        """
        Поиск с учетом регистронезависимости
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза',
                   'рОзА цветок', 'РОЗА упала'])]

        keywords = ["Роза"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора", "рОзА цветок", "РОЗА упала"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_several_filters(self):
        """
        Несколько фильтров
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза',
                   'автобус энергетиков'])]

        keywords = ["Роза", "автобус"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора", "автобус энергетиков"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_several_filters_in_str(self):
        """
        Совпадение нескольких фильтров в одной строке
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза',
                   'на азОра свалилась роза'])]

        keywords = ["Роза", "азора"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора", "на азОра свалилась роза"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_filter_eq_str(self):
        """
        Слово фильтр целиком совпадает со строкой в файле
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза'])]

        keywords = ['розан']

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = ["Розан"]

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_no_answer(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        корректно работает, когда нет строк, содержащих ключевые слова.
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = \
            [iter(['А роЗа Упала На лапу азора', 'Розан', 'ароза'])]

        keywords = ["Стол"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = []

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_empty_file(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        корректно работает при пустом файле.
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = [iter([])]
        keywords = ["Роза"]

        func_result = filter_lines_by_keywords(file_mock(), keywords)
        results = list(func_result)

        expected = []

        self.assertEqual(results, expected)

    def test_filter_lines_by_keywords_error_file_name(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        обрабатывает ошибку, когда указан неверный путь к файлу.
        """
        keywords = ["Роза"]

        file_name = "not_exist.txt"

        with self.assertRaises(FileNotFoundError):
            list(filter_lines_by_keywords(file_name, keywords))

    def test_filter_lines_by_keywords_unread_file(self):
        """
        Проверяет, что функция filter_lines_by_keywords
        обрабатывает ошибку, когда передан неразрешенный файловый объект.
        """
        file_mock = mock.Mock()
        file_mock.return_value = mock.MagicMock()
        file_mock.return_value.__iter__.side_effect = [iter([])]
        del file_mock.return_value.read

        keywords = ["Роза"]

        with self.assertRaises(TypeError):
            list(filter_lines_by_keywords(file_mock, keywords))

    def test_file_obj_no_words_list(self):
        """
        Проверяет корректность работы с текстовым файлом,
        переданным в виде названия
        """
        temp_file = "test_file.txt"

        with open(temp_file, "w", encoding='utf-8') as test_file:
            test_file.write("А роЗа Упала На лапу азора\nРозан\nароза")

        keywords = ["Роза"]

        func_result = filter_lines_by_keywords(temp_file, keywords)
        results = list(func_result)

        expected = ["А роЗа Упала На лапу азора"]

        self.assertEqual(results, expected)

        os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()
