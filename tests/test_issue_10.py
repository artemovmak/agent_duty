"""Regression test for issue #10: search must be ё/е-insensitive."""
import unittest

from shop.catalog import search


class SearchYoTest(unittest.TestCase):
    def test_search_yo_in_query_finds_product(self):
        # «ёлка» in query, product name contains «Ёлка»
        self.assertEqual(search("ёлка"), ["n1"])

    def test_search_e_in_query_finds_yo_product(self):
        # «елка» (without ё) in query, product name contains «Ёлка»
        self.assertEqual(search("елка"), ["n1"])

    def test_search_yo_brush_in_query(self):
        # «щётка» in query, product name contains «Щётка»
        self.assertEqual(search("щётка"), ["h1"])

    def test_search_e_brush_in_query(self):
        # «щетка» (without ё) in query, product name contains «Щётка»
        self.assertEqual(search("щетка"), ["h1"])


if __name__ == "__main__":
    unittest.main()
