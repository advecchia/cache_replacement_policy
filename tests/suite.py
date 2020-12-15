import unittest
from test_case_lru_cache_memory import LRUCacheMemoryTestCase

def build_suite():
    suite = unittest.TestSuite()
    suite.addTest(LRUCacheMemoryTestCase('LRU cache memory tests'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(build_suite())