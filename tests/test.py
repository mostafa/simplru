#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import simplru


def test_simplru():
    @simplru.simplru(max_size=10)
    def multiply(x):
        return (x * 2)

    for i in [1, 2, 3, 4, 5, 6, 6, 5, 5, 4, (1, 2), (1, 2), 1, "A", "B", "A"]:
        multiply(i)

    simplru.cache_info()

    assert len(simplru.cache) == 9
    assert simplru.max_size == 10
    assert simplru.hits == 7
    assert simplru.misses == 9

    for j in range(2):
        for i in [4, 5, 100, 9, 5, 6, 6, 5, 5, 4, (2, 2), (1, 2), "C", "B"]:
            multiply(i)

    assert len(simplru.cache) == 10
    assert simplru.max_size == 10
    assert simplru.hits == 31
    assert simplru.misses == 13

    simplru.cache_clear()


def test_none():
    @simplru.simplru(max_size=2)
    def test_none(x):
        print (x)
        return None

    for x in [1, 1, 1, 2, 2, 3, 3, 4, 5, 6]:
        test_none(x)

    simplru.cache_info()

    assert len(simplru.cache) == 2
    assert simplru.max_size == 2
    assert simplru.hits == 4
    assert simplru.misses == 6


if __name__ == "__main__":
    subprocess.call(["pytest", "test.py"])
