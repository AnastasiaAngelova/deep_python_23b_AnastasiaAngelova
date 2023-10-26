import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)

    def test_zero_limit(self):
        with self.assertRaises(ValueError):
            LRUCache(0)

    def test_str_limit(self):
        with self.assertRaises(TypeError):
            LRUCache("1")

    def test_float_limit(self):
        with self.assertRaises(TypeError):
            LRUCache(1.0)

    def test_old_delete(self):
        lru = LRUCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.set("key3", 3)
        self.assertEqual(lru.get("key2"), 2)
        self.assertEqual(lru.get("key3"), 3)
        with self.assertRaises(KeyError):
            lru.get("key1")

    def test_get(self):
        lru = LRUCache(1)
        lru.set("key1", 1)
        self.assertEqual(lru.get("key1"), 1)

    def test_rewrite(self):
        lru = LRUCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.set("key2", 3)
        self.assertEqual(lru.get("key1"), 1)
        self.assertEqual(lru.get("key2"), 3)

    def test_get_up(self):
        lru = LRUCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.get("key1")
        lru.set("key3", 3)
        self.assertEqual(lru.get("key1"), 1)
        self.assertEqual(lru.get("key3"), 3)
        with self.assertRaises(KeyError):
            lru.get("key2")

    def test_get_non_exist_key(self):
        lru = LRUCache(2)
        with self.assertRaises(KeyError):
            lru.get("key1")


if __name__ == "__main__":
    unittest.main()
