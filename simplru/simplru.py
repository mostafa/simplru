#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import traceback
import os
from collections import OrderedDict


cache = OrderedDict()
hits = 0
max_size = 100
misses = 0


def cache_clear():
    '''
    Resets all (global) variables
    '''
    global cache
    global hits
    global max_size
    global misses

    cache = OrderedDict()
    hits = 0
    max_size = 100
    misses = 0


def cache_info():
    '''
    Returns the current state of LRU cache
    '''
    format_string = "misses={}, hits={}, max={}, currsize={}"
    print(format_string.format(misses, hits, max_size, len(cache)))


def simplru(*cache_args, **cache_kwargs):
    '''
    Top-level decorator to wrap a function for caching (LRU caching)
    '''
    global cache
    global hits
    global max_size
    global misses

    if "max_size" in cache_kwargs:
        if cache_kwargs["max_size"] is None:
            pass
        else:
            max_size = cache_kwargs["max_size"]

    def cache_decorator(func):
        '''
        Actual decorator use cache
        '''
        @wraps(func)
        def wrapped(*args):
            global cache
            global hits
            global misses

            try:
                key = (func.__name__, args)

                if key in cache:
                    if "DEBUG" in os.environ:
                        print "DEBUG: Used cache"

                    cache[key] = cache.pop(key)

                    hits += 1
                else:
                    if "DEBUG" in os.environ:
                        print "DEBUG: Cached value"

                    misses += 1

                    if len(cache) >= max_size:
                        cache.popitem(last=False)

                    cache[key] = func(*args)

                return cache[key]
            except Exception as e:
                if "DEBUG" in os.environ:
                    traceback.print_exc()
                raise(e)
        return wrapped
    return cache_decorator


if __name__ == "__main__":
    @simplru(max_size=10)
    def multiply(x):
        return x * 2

    for i in [1, 2, 3, 4, 5, 6, 6, 5, 5, 4, (1, 2), (1, 2), "A", "B", "A"]:
        multiply(i)

    cache_info()

    for j in range(2):
        for i in [4, 5, 100, 9, 5, 6, 6, 5, 5, 4, (2, 2), (1, 2), "C", "B"]:
            multiply(i)

    cache_info()
    cache_clear()
    cache_info()

    @simplru(max_size=2)
    def test_none(x):
        print x
        return None

    for x in [1, 1, 1, 2, 2, 3, 3, 4, 5, 6]:
        test_none(x)

    cache_info()
