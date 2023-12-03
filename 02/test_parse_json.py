"""HW2 tests for JSON parser"""
import unittest
from unittest.mock import Mock, call

from parse_json import parse_json


class TestTask(unittest.TestCase):
    """
    Tests for JSON parser
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

    def test_parse_json_no_required_fields(self):
        """
        no required_fields
        """
        json_str = '{"key1": "Word1 word2"}'

        with self.assertRaises(ValueError):
            parse_json(json_str)

    def test_parse_json_no_keyword(self):
        """
        no keyword
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]

        with self.assertRaises(ValueError):
            parse_json(json_str, required_fields)

    def test_parse_json_no_keyword_callback(self):
        """
        no keyword_callback
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]
        keyword = ["word2"]

        with self.assertRaises(ValueError):
            parse_json(json_str, required_fields, keyword)

    def test_parse_json_wrong_json(self):
        """
        wrong json
        """
        json_str = 'wrong_json'
        required_fields = ["key1"]
        keyword = ["word2"]
        keyword_callback = Mock()

        with self.assertRaises(ValueError):
            parse_json(json_str, required_fields, keyword, keyword_callback)

    def test_parse_json_1_keyword(self):
        """
        1 in
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]
        keyword = ["word1"]
        keyword_callback = Mock()
        expected_calls = [call(['key1', 'Word1'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_some_keywords(self):
        """
        2 in
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]
        keyword = ["word1", "word2"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']),
                          call(['key1', 'word2'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_missing_keyword(self):
        """
        calls
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]
        keyword = ["word1", "word2", "word3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']), call(['key1', 'word2'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_some_keys(self):
        """
        calls
        """
        json_str = '{"key1": "Word1 word2", "key2": "Word3 word4"}'
        required_fields = ["key1"]
        keyword = ["word1", "word2", "word3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']),
                          call(['key1', 'word2'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_some_required_fields(self):
        """
        calls
        """
        json_str = '{"key1": "Word1 word2", "key2": "Word3 word4"}'
        required_fields = ["key1", "key2"]
        keyword = ["word1", "word2", "word3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']),
                          call(['key1', 'word2']),
                          call(['key2', 'Word3'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_different_register(self):
        """
        different register
        """
        json_str = '{"key1": "word1 woRD2 WORD3",' \
                   '"key2": "woRD1 word2 word3",' \
                   '"key3": "WORD1 WORD2 woRD3"}'
        required_fields = ["key1", "key2", "key3"]
        keyword = ["word1", "woRD2", "WORD3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'word1']),
                          call(['key1', 'woRD2']),
                          call(['key1', 'WORD3']),
                          call(['key2', 'woRD1']),
                          call(['key2', 'word2']),
                          call(['key2', 'word3']),
                          call(['key3', 'WORD1']),
                          call(['key3', 'WORD2']),
                          call(['key3', 'woRD3'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_part_of_a_word(self):
        """
        parse of a word (False)
        """
        json_str = '{"key1": "my word", ' \
                   '"key2": "my_word", ' \
                   '"key3": "word1"}'
        required_fields = ["key1", "key2", "key3"]
        keyword = ["word"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'word'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, expected_calls)

    def test_parse_json_empty_required_fields(self):
        """
        empty required fields
        """
        json_str = '{"key1": "word"}'
        required_fields = []
        keyword = ["word"]

        with self.assertRaises(ValueError):
            parse_json(json_str, required_fields, keyword)

    def test_parse_json_no_json_key_of_required_fields(self):
        """
        no json key of required fields
        """
        json_str = '{"key1": "word"}'
        required_fields = ["wrong key"]
        keyword = ["word"]
        keyword_callback = Mock()

        parse_json(json_str, required_fields, keyword, keyword_callback)
        self.assertEqual(keyword_callback.mock_calls, [])


if __name__ == '__main__':
    unittest.main()
