import unittest
from unittest import mock
from unittest.mock import Mock, call

from server import Server
from client import Client


class TestServerClient(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_server_connection(self):
        host = "127.0.0.1"
        port = 8080
        server = Server(host, port, 2, 10)
        self.assertEqual(server.server.getsockname(), (host, port))

    def test_client_connection(self):
        host = "localhost"
        port = 8080
        client = Client(host, port, 2, "test.txt")
        self.assertEqual(client.host, host)
        self.assertEqual(client.port, port)
        self.assertEqual(client.thread_count, 2)

    def test_get_words_count_json(self):
        server = Server("127.0.0.1", 8080, 10, 7)
        text = "This is a sample text for testing. This is a sample."
        result = server.get_words_count_json(text)
        expected = '{"this": 2, "is": 2, "a": 2, "sample": 2, "text": 1, "for": 1, "testing": 1}'
        self.assertEqual(expected, result)

    def test_connect(self):
        with open('mock_file.txt', 'w') as file:
            file.write("\n")

        with mock.patch("builtins.print") as mock_print:
            Server("127.0.0.1", 8080, 10, 7)
            Client("127.0.0.1", 8080, 10, file)

        expected = [call('Сonnection to host 127.0.0.1 on port 8080 established')]
        self.assertEqual(expected, mock_print.call_args_list)

    def test_server_negative_w(self):
        with self.assertRaises(ValueError):
            Server("127.0.0.1", 8080, -10, 7)

    def test_server_negative_k(self):
        with self.assertRaises(ValueError):
            Server("127.0.0.1", 8080, 10, -7)

    def test_server_zero_w(self):
        with self.assertRaises(ValueError):
            Server("127.0.0.1", 8080, 0, 7)

    def test_server_zero_k(self):
        with self.assertRaises(ValueError):
            Server("127.0.0.1", 8080, 10, 0)

    def test_client_negative_M(self):
        with open('mock_file.txt', 'w') as file:
            file.write("\n")
        with self.assertRaises(ValueError):
            Client("127.0.0.1", 8080, -5, file)

    def test_client_zero_M(self):
        with open('mock_file.txt', 'w') as file:
            file.write("\n")
        with self.assertRaises(ValueError):
            Client("127.0.0.1", 8080, 0, file)

if __name__ == '__main__':
    unittest.main()
