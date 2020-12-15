import unittest
import io
from domain.cache_memory import CacheItem, LRUCacheMemory
from contextlib import redirect_stdout, redirect_stderr

class LRUCacheMemoryTestCase(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCacheMemory()

    def tearDown(self):
        self.cache = None

    def test_should_fail_to_create_a_cache(self):
        """Will fail to create a new cache because it will break the minimum size.
        """
        print('Will fail to create a new cache because it will break the minimum size.')

        try:
            self.cache = LRUCacheMemory(0)

        except ValueError as e:
            self.assertEqual('Invalid value for memory size: need to be greater than zero.', str(e))

    def test_should_create_an_empty_cache(self):
        """Will verify cache emptiness.
        """
        print('Will verify cache emptiness.')

        memory = self.cache.get_memory()
        self.assertEqual(0, len(memory))

    def test_should_add_one_item_to_cache(self):
        """Will add an item to cache and verify.
        """
        print('Will add an item to cache and verify.')

        content = 'A'
        item = CacheItem(content)
        self.cache.add(item)

        memory = self.cache.get_memory()
        self.assertEqual(1, len(memory))

        item = memory[0]
        self.assertEqual(content, item[0])
        self.assertEqual(1, item[1])

    def test_should_print_current_empty_memory_to_output(self):
        """Will print the current empty memory to output.
        """
        print('Will print the current empty memory to output.')

        string_io = io.StringIO()
        with redirect_stdout(string_io):
            self.assertEqual(None, self.cache.lookup())

        output = string_io.getvalue()
        self.assertEqual('Memory is empty\n', output)

    def test_should_print_current_memory_with_one_item_to_output(self):
        """Will print the current memory with one item to output.
        """
        print('Will print the current memory with one item to output.')

        content = 'A'
        item = CacheItem(content)
        self.cache.add(item)

        memory = self.cache.get_memory()
        item = memory[0]
        self.assertEqual(content, item[0])
        self.assertEqual(1, item[1])

        string_io = io.StringIO()
        with redirect_stdout(string_io):
            self.assertEqual(None, self.cache.lookup())

        output = string_io.getvalue()
        self.assertEqual('Memory: [A(1)]\n', output)

    def test_should_print_current_memory_with_some_items_to_output(self):
        """Will print the current memory with some items to output.
        """
        print('Will print the current memory with some items to output.')

        seq = ['A', 'B', 'C', 'D', 'B', 'B', 'C', 'A', 'C', 'D']
        for content in seq:
            item = CacheItem(content)
            self.cache.add(item)

        memory = self.cache.get_memory()
        self.assertEqual(4, len(memory))

        string_io = io.StringIO()
        with redirect_stdout(string_io):
            self.assertEqual(None, self.cache.lookup())

        output = string_io.getvalue()
        self.assertEqual('Memory: [B(6), C(9), A(8), D(10)]\n', output)