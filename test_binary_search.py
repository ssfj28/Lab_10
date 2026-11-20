"""Проверка функции бинарного поиска стандартным модулем unittest."""

import unittest

from binary_search import binary_search, is_sorted_ascending


class BinarySearchTests(unittest.TestCase):
    def test_find_middle_element(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_find_first_element(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 1), 0)

    def test_find_last_element(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 4)

    def test_value_is_absent(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 6), -1)

    def test_negative_values(self):
        self.assertEqual(binary_search([-10, -5, -1, 0, 4], -5), 1)

    def test_empty_array(self):
        self.assertEqual(binary_search([], 10), -1)

    def test_single_element_array(self):
        self.assertEqual(binary_search([8], 8), 0)
        self.assertEqual(binary_search([8], 3), -1)

    def test_duplicates_return_a_matching_index(self):
        values = [1, 2, 2, 2, 5]
        index = binary_search(values, 2)
        self.assertNotEqual(index, -1)
        self.assertEqual(values[index], 2)

    def test_sorted_check(self):
        self.assertTrue(is_sorted_ascending([-2, 0, 0, 5]))
        self.assertFalse(is_sorted_ascending([1, 5, 3, 7]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
