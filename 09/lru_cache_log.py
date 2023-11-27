import argparse
import logging
import logging.config


class LruCache:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, limit, log):
        self.log = log

        if not isinstance(limit, int):
            self.log.error("limit must be int, input limit: %s", limit)
            raise TypeError("limit must be int")
        if limit <= 0:
            self.log.error("limit must be positive, input linit: %s", limit)
            raise ValueError("limit must be positive")

        self.limit = limit

        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.log.debug("init LruCache")

    def get(self, key):
        self.log.debug("start get")
        if key not in self.cache:
            self.log.error("key doesn't exist")
            raise KeyError("key doesn't exist")

        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)

        self.log.info("get node: (%s:%s)", key, node.value)
        return node.value

    def set(self, key, value):
        self.log.debug("start set")
        if key in self.cache:
            self.log.info("delete to rewrite key: (%s:%s)",
                          key, self.cache[key].value)
            self.remove_node(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self.add_node(node)
        self.log.info("add node: (%s:%s)", key, value)
        if len(self.cache) > self.limit:
            self.log.info("Delete oldest cache node: (%s:%s)",
                          self.head.next.key, self.head.next.value)
            node = self.head.next
            self.remove_node(node)
            del self.cache[node.key]

        if len(self.cache) == self.limit:
            self.log.warning("cache full: %s/%s", len(self.cache), self.limit)
        elif len(self.cache) >= self.limit / 2:
            self.log.warning("cache almost full: %s/%s",
                             len(self.cache), self.limit)

    @staticmethod
    def remove_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node


def get_logger(s, f):
    handlers = ["file_handler"]
    if s:
        handlers.append("stream_handler")

    conf = {
        "version": 1,
        "formatters": {
            "formatter": {
                "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s",
            },
        },
        "handlers": {
            "stream_handler": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "formatter",
            },
            "file_handler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "formatter",
                "filename": "cache.log",
                "mode": "w",
            },
        },
        "loggers": {
            "": {
                "level": "DEBUG",
                "handlers": handlers,
                "propagate": False,
            },

        },
    }

    logging.config.dictConfig(conf)
    logger = logging.getLogger()

    if f:
        class EvenWordCountFilter(logging.Filter):
            def filter(self, record):
                message = record.getMessage()
                word_count = len(message.split())
                return word_count % 2 == 0

        logger.handlers[handlers.index("stream_handler")]\
            .addFilter(EvenWordCountFilter())

        class OddWordCountFilter(logging.Filter):
            def filter(self, record):
                message = record.getMessage()
                word_count = len(message.split())
                return word_count % 2 != 0

        logger.handlers[handlers.index("file_handler")]\
            .addFilter(OddWordCountFilter())

    return logger


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="lru_cache_log")
    parser.add_argument("-s", action='store_true', help="log stdout")
    parser.add_argument("-f", action='store_true', help="log filter")
    args = parser.parse_args()

    lru_logger = get_logger(args.s, args.f)

    lru = LruCache(3, lru_logger)

    lru.set("key1", "value1")   # set missing key
    lru.set("key2", "value2")   # set missing key
    lru.set("key3", "value3")   # set missing key
    lru.set("key1", "value1_update")    # set existing key
    lru.get("key2")     # get existing key

    try:
        lru.get("key-1")    # get missing key
    except KeyError:
        pass

    lru.set("key4", "value4")   # set missing key when capacity reached
