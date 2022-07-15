# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testing.py
@Time    :  2022/7/15 15:21 PM
@Author  :  YuYanQing
@Version :  0.0.1
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  Define helper functions for testing.
"""

from pprint import pformat

from . import diff


def assert_no_diff(*args, **kwargs):
    """Compare two dictionary/list/set objects and raise error on difference.

    When there is a difference, this will print a formatted diff.
    This is especially useful for pytest.

    Usage example:

        >>> from dictdiffer.testing import assert_no_diff
        >>> result = {'a': 'b'}
        >>> expected = {'a': 'c'}
        >>> assert_no_diff(result, expected)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 14, in assert_no_diff
        AssertionError: [('change', 'a', ('b', 'c'))]

    :param args: Positional arguments to the ``diff`` function.
    :param second: Named arguments to the ``diff`` function.
    """
    d = [d for d in diff(*args, **kwargs)]
    assert not d, pformat(d)
