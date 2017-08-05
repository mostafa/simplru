from setuptools import setup

setup(name="simplru",
      version="0.0.1",
      description="A backport of Python 3 LRU Cache functionality for Python 2",
      url="https://github.com/mostafa/simplru",
      author="Mostafa Moradian",
      author_email="mostafamoradian0@gmail.com",
      license="GPLv3",
      packages=["simplru"],
      long_description="""
Simplru
=====

A backport of Python 3 LRU Cache functionality for Python 2

For more information, visit github page of `the project <https://github.com/mostafa/simplru>`_.""",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3"
      ],
      # keywords='',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
