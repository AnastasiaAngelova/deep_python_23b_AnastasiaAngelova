import unittest
from lru_cache import LruCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            LruCache(-1)

    def test_zero_limit(self):
        with self.assertRaises(ValueError):
            LruCache(0)

    def test_str_limit(self):
        with self.assertRaises(TypeError):
            LruCache("1")

    def test_float_limit(self):
        with self.assertRaises(TypeError):
            LruCache(1.0)

    def test_old_delete(self):
        lru = LruCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.set("key3", 3)
        self.assertEqual(lru.get("key2"), 2)
        self.assertEqual(lru.get("key3"), 3)
        with self.assertRaises(KeyError):
            lru.get("key1")

    def test_get(self):
        lru = LruCache(1)
        lru.set("key1", 1)
        self.assertEqual(lru.get("key1"), 1)

    def test_rewrite(self):
        lru = LruCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.set("key2", 3)
        self.assertEqual(lru.get("key1"), 1)
        self.assertEqual(lru.get("key2"), 3)

    def test_get_up(self):
        lru = LruCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)
        lru.get("key1")
        lru.set("key3", 3)
        self.assertEqual(lru.get("key3"), 3)
        with self.assertRaises(KeyError):
            lru.get("key2")

    def test_get_non_exist_key(self):
        lru = LruCache(2)
        with self.assertRaises(KeyError):
            lru.get("key1")

    def test_limit_1(self):
        lru = LruCache(1)
        lru.set("key1", 1)
        self.assertEqual(lru.get("key1"), 1)

        lru.set("key2", 2)
        with self.assertRaises(KeyError):
            lru.get("key1")

    def test_delete_old(self):
        lru = LruCache(2)
        lru.set("key1", 1)
        lru.set("key2", 2)  # cache = {"key1":1, "key2":2}
        lru.get("key1")     # cache = {"key2":2, "key1":1}
        lru.set("key3", 3)  # cache = {"key1":1, "key3":3}

        with self.assertRaises(KeyError):
            lru.get("key2")

        lru.set("key1", 11)     # cache = {"key3":3, "key1":11}
        lru.set("key4", 4)  # cache = {"key1":11, "key4":4}

        with self.assertRaises(KeyError):
            lru.get("key3")

        self.assertEqual(lru.get("key1"), 11)
        self.assertEqual(lru.get("key4"), 4)


if __name__ == "__main__":
    unittest.main()
