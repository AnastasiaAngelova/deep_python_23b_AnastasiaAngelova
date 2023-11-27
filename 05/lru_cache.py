class LruCache:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, limit=42):
        if not isinstance(limit, int):
            raise TypeError("limit must be int")
        if limit <= 0:
            raise ValueError("limit must be positive")
        self.limit = limit
        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            raise KeyError("key doesn't exist")
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            self.remove_node(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self.add_node(node)
        if len(self.cache) > self.limit:
            node = self.head.next
            self.remove_node(node)
            del self.cache[node.key]

    @staticmethod
    def remove_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
