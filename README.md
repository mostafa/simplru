# Simplru
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmostafa%2Fsimplru.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmostafa%2Fsimplru?ref=badge_shield)

A backport of Python 3 LRU Cache functionality for Python 2

## Installation
To install simplru, you can use setuptools (install from source) or another python package manager (e.g. pip or easy_install).

+ To install from `source code`, clone the repository (you should have git installed) and then run setup.py:
```bash
$ git clone https://github.com/mostafa/simplru.git
$ cd simplru
$ python setup.py install
```
+ To install using a python package manager via `binary package`, simply run this command (in this case we've used pip, but any package manager is accepted as long as it uses [PyPI](https://pypi.python.org/pypi)):
```bash
$ pip install simplru
```

### Edit mode installation
```bash
$ cd path/to/project
$ pip install -e .
```

## Tests
You can find an tests in [tests](https://github.com/mostafa/simplru/tree/master/tests) directory.

## Examples
Refer to [Python 3 documentation](https://docs.python.org/3/library/functools.html#functools.lru_cache) for examples of LRU cache usage.


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmostafa%2Fsimplru.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmostafa%2Fsimplru?ref=badge_large)