#!/usr/bin/env python

import contextlib
import csv
import os
import tempfile
import unittest

from query import query


@contextlib.contextmanager
def csv_file(data):

    f = tempfile.NamedTemporaryFile(delete=False)
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()

    yield f.name

    os.remove(f.name)


class TestQuery(unittest.TestCase):

    def test_no_rows(self):
        with csv_file([]) as filename:
            rows = query(filename, 0, "a")
            self.assertEqual(rows, [])

    def test_single_row(self):
        with csv_file([["a"]]) as filename:
            rows = query(filename, 0, "a")
            self.assertEqual(rows, [["a"]])

    def test_single_row_doesnt_match(self):
        with csv_file([["a"]]) as filename:
            rows = query(filename, 0, "b")
            self.assertEqual(rows, [])

    def test_multiple_rows(self):
        with csv_file([["a"], ["a"]]) as filename:
            rows = query(filename, 0, "a")
            self.assertEqual(rows, [["a"], ["a"]])

    def test_multiple_rows_dont_all_match(self):
        with csv_file([["a"], ["b"]]) as filename:
            rows = query(filename, 0, "b")
            self.assertEqual(rows, [["b"]])


if __name__ == '__main__':
    unittest.main()
