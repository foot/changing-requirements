#!/usr/bin/env python


import csv
import tempfile
import unittest

from query import query


class TestQuery(unittest.TestCase):

    def csv_file(self, data):

        f = tempfile.NamedTemporaryFile()
        writer = csv.writer(f)
        writer.writerows(data)

        return f.name

    def test_no_rows(self):
        filename = self.csv_file([])
        rows = query(filename, 0, 1)
        self.assertEqual(rows, [])

    def test_single_row(self):
        filename = self.csv_file([[1]])
        rows = query(filename, 0, 1)
        self.assertEqual(rows, [[1]])

    def test_single_row_doesnt_match(self):
        filename = self.csv_file([[1]])
        rows = query(filename, 0, 2)
        self.assertEqual(rows, [])

    def test_multiple_rows(self):
        filename = self.csv_file([[1], [1]])
        rows = query(filename, 0, 1)
        self.assertEqual(rows, [[1], [1]])

    def test_multiple_rows_dont_all_match(self):
        filename = self.csv_file([[1], [2]])
        rows = query(filename, 0, 2)
        self.assertEqual(rows, [[2]])


if __name__ == '__main__':
    unittest.main()
