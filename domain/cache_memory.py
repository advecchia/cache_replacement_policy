from abc import ABC
from abc import abstractmethod
import sys

DEFAULT_CACHE_SIZE = 4

class CacheMemory(ABC):
    """CacheMemory base class will represent a single memory for cacheable objects."""

    def __init__(self, size):
        """Class constructor.

        Args:
            size (int): A number that represents the memory size.
        """
        #try:
        self.age = 0
        self.cache = dict()
        self.size = int(size)
        if (self.size < 1):
            raise ValueError('Invalid value for memory size: need to be greater than zero.')

    @abstractmethod
    def add(self, item):
        raise NotImplementedError('Please implement the add() method')

    def _aging(self):
        self.age += 1

    def _has_space(self):
        return len(self.cache) < self.size

    def _contains(self, item):
        if not item:
            raise ValueError('Cacheable object can not be null.')

        return item.get() in self.cache

    def lookup(self):
        if not self.cache:
            print('Memory is empty')
            return

        items = list()
        for item in self.cache.values():
            items.append(' {}({})'.format(item[1].get(), item[0]))
        print('Memory: [' + ','.join(items).strip() + ']')

    def get_memory(self):
        items = list()

        if not self.cache:
            return items

        for item in self.cache.values():
            items.append((item[1].get(), item[0]))

        return items


class LRUCacheMemory(CacheMemory):
    """LRUCacheMemory class will represent a single memory for cacheable objects."""

    def __init__(self, size=DEFAULT_CACHE_SIZE):
        """Class constructor.

        Args:
            size (int, optional): A number that represents the memory size. Defaults to DEFAULT_CACHE_SIZE.
        """
        super().__init__(size)

    def _get_oldest_item(self):
        return min(self.cache.values(), key=lambda item: item[0])

    def _get_newest_item(self):
        return max(self.cache.values(), key=lambda item: item[0])

    def add(self, item):
        # Least recently used (LRU)
        if not item:
            raise ValueError('Cacheable object can not be null.')

        # increase age for newer item
        self._aging()
        if not self._has_space():
            # has no free space
            oldest = self._get_oldest_item()
            del self.cache[oldest[1].get()]

        self.cache[item.get()] = [self.age, item]


class CacheItem():
    """CacheItem class will represent a single cacheable object."""

    def __init__(self, content):
        """Class constructor.

        Args:
            content (str): A string that represents a name or content for a cacheable object.
        """        
        self.content = content

    def get(self):
        return self.content