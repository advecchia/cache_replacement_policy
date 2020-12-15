from domain.cache_memory import LRUCacheMemory, CacheItem, DEFAULT_CACHE_SIZE

"""Cache Replacement Policy (CRP)

Toy implementation to try different CRP's.
"""
DEFAULT_SEQUENCE = ['A', 'B', 'C', 'D', 'B', 'B', 'C', 'A', 'C', 'D']

def prepare():
    return LRUCacheMemory(DEFAULT_CACHE_SIZE)

def run(cache):
    for content in DEFAULT_SEQUENCE:
        cache.add(CacheItem(content))
    return cache

def check(cache):
    cache.lookup()

def main():
    cache = prepare()
    cache = run(cache)
    check(cache)


if __name__ == '__main__':
    main()