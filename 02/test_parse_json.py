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

    def test_parse_json_wrong_key(self):
        """
        if key error
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["wrong_key"]
        keyword = ["word2"]
        keyword_callback = Mock()

        with self.assertRaises(KeyError):
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
        keyword_callback.assert_has_calls(expected_calls)

    def test_parse_json_some_keywords(self):
        """
        2 in
        """
        json_str = '{"key1": "Word1 word2"}'
        required_fields = ["key1"]
        keyword = ["word1", "word2"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']), call(['key1', 'word2'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        keyword_callback.assert_has_calls(expected_calls, any_order=False)

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
        keyword_callback.assert_has_calls(expected_calls)

    def test_parse_json_some_keys(self):
        """
        calls
        """
        json_str = '{"key1": "Word1 word2", "key2": "Word3 word4"}'
        required_fields = ["key1"]
        keyword = ["word1", "word2", "word3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']), call(['key1', 'word2'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        keyword_callback.assert_has_calls(expected_calls)

    def test_parse_json_some_required_fields(self):
        """
        calls
        """
        json_str = '{"key1": "Word1 word2", "key2": "Word3 word4"}'
        required_fields = ["key1", "key2"]
        keyword = ["word1", "word2", "word3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1']), call(['key1', 'word2']), call(['key2', 'Word3'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        keyword_callback.assert_has_calls(expected_calls)

    def test_parse_json_part_of_a_word(self):
        """
        keyword is a part of a word
        """
        json_str = '{"key1": "Word1_old new_Word2", "key2": "full_Word3.txt word4"}'
        required_fields = ["key1", "key2"]
        keyword = ["Word1", "wOrd2", "worD3"]
        keyword_callback = Mock()

        expected_calls = [call(['key1', 'Word1_old']),
                          call(['key1', 'new_Word2']),
                          call(['key2', 'full_Word3.txt'])]

        parse_json(json_str, required_fields, keyword, keyword_callback)
        keyword_callback.assert_has_calls(expected_calls)

    def test_parse_json_empty_required_fields(self):
        """
        empty required fields
        """
        json_str = '{"key1": "Word1_old new_Word2", "key2": "full_Word3.txt word4"}'
        required_fields = []
        keyword = ["Word1", "wOrd2", "worD3"]

        with self.assertRaises(ValueError):
            parse_json(json_str, required_fields, keyword)


if __name__ == '__main__':
    unittest.main()
