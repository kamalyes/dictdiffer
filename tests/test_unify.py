import unittest

from dictdiffer.conflict import Conflict
from dictdiffer.unify import Unifier
from dictdiffer.utils import nested_hash


class TestUnifier(unittest.TestCase):

    def test_build_index(self):
        u = Unifier()

        p1 = ('add', 'foo', [(0, 0)])
        p2 = ('add', 'foo', [(0, 1)])
        c = Conflict(p1, p2)

        u._build_index([c])

        self.assertEqual(u._index[nested_hash(p1)], c)
        self.assertEqual(u._index[nested_hash(p2)], c)

    def test_unify(self):
        u = Unifier()

        p1 = ('add', 'foo', [(0, 0)])
        p2 = ('add', 'foo', [(0, 1)])
        c = Conflict(p1, p2)
        c.take = 'f'

        u.unify([p1], [p2], [c])

        self.assertEqual(u.unified_patches, [p1])
