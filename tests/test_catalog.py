import unittest

from shop.catalog import normalize, search


class CatalogTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("Ёлка"), "елка")

    def test_search(self):
        self.assertEqual(search("чайник"), ["k1", "k2"])
        self.assertEqual(search("  тостер "), ["t1"])
        self.assertEqual(search("пылесос"), [])


if __name__ == "__main__":
    unittest.main()
