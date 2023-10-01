"""Тесты к заданию 1 ДЗ 1"""
import unittest
from unittest import mock

from predict_message_mood import (predict_message_mood,
                                  SomeModel, check_thresholds)


class TestPredictMessageMood(unittest.TestCase):
    """
    Набор тестов для функции `predict_message_mood` и связанных функций.
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

    def test_normal_mood(self):
        """
        Проверяет, что функция корректно определяет нормальное настроение.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.5

            result = predict_message_mood("Пример сообщения", SomeModel())

            self.assertEqual(result, "норм")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_good_mood(self):
        """
        Проверяет, что функция корректно определяет хорошее настроение.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.8

            result = predict_message_mood("Пример сообщения", SomeModel())

            self.assertEqual(result, "отл")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_bad_mood(self):
        """
        Проверяет, что функция корректно определяет плохое настроение.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.1

            result = predict_message_mood("Пример сообщения", SomeModel())

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_user_thresholds(self):
        """
        Проверяет, что пользовательские пороги корректно применяются.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.7

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.8, 0.9)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_invalid_type_thresholds(self):
        """
        Проверяет, что функция `check_thresholds` обнаруживает некорректные типы порогов.
        """
        with self.assertRaises(ValueError):
            check_thresholds("invalid", 0.8)

        with self.assertRaises(ValueError):
            check_thresholds(0.3, "invalid")

        with self.assertRaises(ValueError):
            check_thresholds("invalid", "invalid")

    def test_bad_threshold_greater_than_good(self):
        """
        Проверяет, что функция `check_thresholds` обнаруживает пороги,
        где плохой порог больше хорошего.
        """
        with self.assertRaises(ValueError):
            check_thresholds(0.9, 0.8)

    def test_invalid_values_range(self):
        """
        Проверяет, что функция `check_thresholds` обнаруживает
        некорректные диапазоны значений порогов.
        """
        with self.assertRaises(ValueError):
            check_thresholds(-1, 0.8)

        with self.assertRaises(ValueError):
            check_thresholds(0.2, 1.2)

        with self.assertRaises(ValueError):
            check_thresholds(1.2, -2)

    def test_empty_message(self):
        """
        Проверяет, что функция `predict_message_mood` обнаруживает пустое сообщение.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.7

            with self.assertRaises(ValueError):
                predict_message_mood("  ", SomeModel(), 0.2, 0.8)


if __name__ == "__main__":
    unittest.main()
