#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from simplru import lru_cache


def test_simplru():
    @lru_cache(maxsize=10)
    def multiply(x):
        return (x * 2)

    for i in [1, 2, 3, 4, 5, 6, 6, 5, 5, 4, (1, 2), (1, 2), 1, "A", "B", "A"]:
        multiply(i)

    print(multiply.cache_info())

    assert multiply.cache_info().currsize == 9
    assert multiply.cache_info().maxsize == 10
    assert multiply.cache_info().hits == 7
    assert multiply.cache_info().misses == 9

    for j in range(2):
        for i in [4, 5, 100, 9, 5, 6, 6, 5, 5, 4, (2, 2), (1, 2), "C", "B"]:
            multiply(i)

    print(multiply.cache_info())

    assert multiply.cache_info().currsize == 10
    assert multiply.cache_info().maxsize == 10
    assert multiply.cache_info().hits == 31
    assert multiply.cache_info().misses == 13

    multiply.cache_clear()


def test_none():
    @lru_cache(maxsize=2)
    def test_none(x):
        print (x)
        return None

    for x in [1, 1, 1, 2, 2, 3, 3, 4, 5, 6]:
        test_none(x)

    print(test_none.cache_info())

    assert test_none.cache_info().currsize == 2
    assert test_none.cache_info().maxsize == 2
    assert test_none.cache_info().hits == 4
    assert test_none.cache_info().misses == 6


if __name__ == "__main__":
    subprocess.call(["pytest", "test.py"])
