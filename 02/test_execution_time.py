""" HW2 tests for execution_time """
import unittest
from unittest import mock
from unittest.mock import Mock, patch

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
            mock_func = execution_time("2")(mock_func)

    def test_execution_time_negative_int(self):
        """
        check if execution time not positive integer
        """
        with self.assertRaises(ValueError):
            mock_func = Mock()
            mock_func = execution_time(-1)(mock_func)

    @mock.patch("time.time")
    def test_execution_time_work(self, mock_time):
        """
        check work of execution time
        """
        mock_time.side_effect = [1.0, 2.0]

        @execution_time(1)
        def test_func():
            pass

        with patch("builtins.print") as mock_print:
            test_func()

        expected_output = "Mean time for last 1 calls: 1.000000 sec"

        mock_print.assert_has_calls(
            [unittest.mock.call(expected_output)]
        )


if __name__ == '__main__':
    unittest.main()
