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
        Передача новых порогов
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.01

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.1, 0.2)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_user_good_threshold_is_equal(self):
        """
        Значение предикта = good_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.4

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.1, 0.4)

            self.assertEqual(result, "отл")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_user_bad_threshold_is_equal(self):
        """
        Значение предикта = bad_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.1

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.1, 0.4)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_user_thresholds_is_equal(self):
        """
        Проверка возвращения "неуд", если bad_threshold == good_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.5

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.5, 0.5)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_invalid_user_thresholds(self):
        """
        bad_threshold > good_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.7

            with self.assertRaises(ValueError):
                predict_message_mood("Пример сообщения", SomeModel(), 1, 0.1)

    def test_critical_good_threshold_value(self):
        """
        good_threshold == 1
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.9

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.5, 1)

            self.assertEqual(result, "норм")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 1

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.5, 1)

            self.assertEqual(result, "отл")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_critical_bad_threshold_value(self):
        """
        Краевой случай порогов - bad_threshold = 0
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.1

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0, 0.4)

            self.assertEqual(result, "норм")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0, 0.4)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_near_critical_bad_threshold_value(self):
        """
        Околокраевой случай порога - bad_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.00000000001, 0.4)

            self.assertEqual(result, "неуд")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_near_critical_invalid_bad_threshold_value(self):
        """
        Околокраевой случай порога - bad_threshold немного меньше самого
        низкого допустимого значения
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0

            with self.assertRaises(ValueError):
                predict_message_mood("Пример сообщения", SomeModel(),
                                     -0.000000000001, 0.4)

    def test_near_critical_good_threshold_value(self):
        """
        Околокраевой случай порога - good_threshold
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 1

            result = predict_message_mood("Пример сообщения", SomeModel(),
                                          0.5, 0.9999999999999)

            self.assertEqual(result, "отл")
            self.assertEqual([mock.call("Пример сообщения")],
                             mock_predict.mock_calls)

    def test_near_critical_invalid_good_threshold_value(self):
        """
        Околокраевой случай порога - good_threshold больше допустимого
        значения
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 1

            with self.assertRaises(ValueError):
                predict_message_mood("Пример сообщения", SomeModel(),
                                     0.5, 1.0000000000001)

    def test_invalid_type_thresholds(self):
        """
        Проверяет, что функция `check_thresholds`
        обнаруживает некорректные типы порогов.
        """
        with self.assertRaises(ValueError):
            check_thresholds("invalid", 0.8)

        with self.assertRaises(ValueError):
            check_thresholds(0.3, "invalid")

        with self.assertRaises(ValueError):
            check_thresholds("invalid", "invalid")

    def test_bad_threshold_greater_than_good(self):
        """
        Плохой порог больше хорошего.
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
        Проверяет, что функция `predict_message_mood` обнаруживает
        пустое сообщение.
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.7

            with self.assertRaises(TypeError):
                predict_message_mood("  ", SomeModel(), 0.2, 0.8)

    def test_message_without_space(self):
        """
        Проверяет, что функция `predict_message_mood`
        корректно обрабатывает строку без пробелов
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 0.7

            result = predict_message_mood("Message", SomeModel(), 0.2, 0.8)

            self.assertEqual(result, "норм")
            self.assertEqual([mock.call("Message")],
                             mock_predict.mock_calls)

    def test_predict_value_out_of_range(self):
        """
        Проверяет, что функция `predict_message_mood`
        корректно обрабатывает случаи
        с неправильным значением предикта
        """
        with mock.patch.object(SomeModel, 'predict') as mock_predict:
            mock_predict.return_value = 1.1

            with self.assertRaises(ValueError):
                predict_message_mood("Message", SomeModel(), 0.2, 0.8)


if __name__ == "__main__":
    unittest.main()
