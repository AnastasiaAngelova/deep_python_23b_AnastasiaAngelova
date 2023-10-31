""" HW2 tests for execution_time """
import unittest
from unittest import mock
from unittest.mock import Mock, call

from execution_time import execution_time


class TestTask(unittest.TestCase):
    """
    Tests for execution_time
    """

    def setUp(self):
        """
        Run before test
        """
        print("setUp")

    def tearDown(self):
        """
        Run after test
        """
        print("tearDown")

    def test_execution_time_not_int(self):
        """
        check if execution time not integer
        """
        with self.assertRaises(TypeError):
            mock_func = Mock()
            execution_time("2")(mock_func)

    def test_execution_time_negative_int(self):
        """
        check if execution time not positive integer
        """
        with self.assertRaises(ValueError):
            mock_func = Mock()
            execution_time(-1)(mock_func)

    @mock.patch("time.time")
    def test_execution_time_1_time(self, mock_time):
        """
        check work of execution time
        """
        mock_time.side_effect = [0.0, 1.0]

        @execution_time(1)
        def test_func():
            pass

        with mock.patch("builtins.print") as mock_print:
            test_func()

        expected = [call('Mean time for last 1 calls: 1.000000 sec')]

        self.assertEqual(expected, mock_print.call_args_list)

    @mock.patch("time.time")
    def test_execution_time_equel_times(self, mock_time):
        """
        check work of execution time
        """
        mock_time.side_effect = [0.0, 1.0,  # 1.0
                                 1.0, 2.5,  # 1.5
                                 2.5, 4.5,  # 2.0
                                 4.5, 5.0,  # 0.5
                                 5.0, 8.0]  # 3.0

        @execution_time(5)
        def test_func():
            pass

        with mock.patch("builtins.print") as mock_print:
            for _ in range(5):
                test_func()

        expected = [call('Mean time for last 1 calls: 1.000000 sec'),
                    call('Mean time for last 2 calls: 1.250000 sec'),
                    call('Mean time for last 3 calls: 1.500000 sec'),
                    call('Mean time for last 4 calls: 1.250000 sec'),
                    call('Mean time for last 5 calls: 1.600000 sec')]

        self.assertEqual(expected, mock_print.call_args_list)

    @mock.patch("time.time")
    def test_execution_time_more_times(self, mock_time):
        """
        check work of execution time
        """
        mock_time.side_effect = [0.0, 1.0,  # 1.0
                                 1.0, 2.5,  # 1.5
                                 2.5, 4.5,  # 2.0
                                 4.5, 5.0,  # 0.5
                                 5.0, 8.0]  # 3.0

        @execution_time(7)
        def test_func():
            pass

        with mock.patch("builtins.print") as mock_print:
            for _ in range(5):
                test_func()

        expected = [call('Mean time for last 1 calls: 1.000000 sec'),
                    call('Mean time for last 2 calls: 1.250000 sec'),
                    call('Mean time for last 3 calls: 1.500000 sec'),
                    call('Mean time for last 4 calls: 1.250000 sec'),
                    call('Mean time for last 5 calls: 1.600000 sec')]

        self.assertEqual(expected, mock_print.call_args_list)

    @mock.patch("time.time")
    def test_execution_time_less_times(self, mock_time):
        """
        check work of execution time
        """
        mock_time.side_effect = [0.0, 1.0,  # 1.0
                                 1.0, 2.5,  # 1.5
                                 2.5, 4.5,  # 2.0
                                 4.5, 5.0,  # 0.5
                                 5.0, 8.0]  # 3.0

        @execution_time(3)
        def test_func():
            pass

        with mock.patch("builtins.print") as mock_print:
            for _ in range(5):
                test_func()

        expected = [call('Mean time for last 1 calls: 1.000000 sec'),
                    call('Mean time for last 2 calls: 1.250000 sec'),
                    call('Mean time for last 3 calls: 1.500000 sec'),
                    call('Mean time for last 3 calls: 1.333333 sec'),
                    call('Mean time for last 3 calls: 1.833333 sec')]

        self.assertEqual(expected, mock_print.call_args_list)


if __name__ == '__main__':
    unittest.main()
