import unittest as ut
from source import file_io as fi
import os as os
import pandas as pd

list_not_strings = [True, 1, 2.3]
list_strings = ["x", "Ab1"]
possible_paths = ["z", "test.csv", ".txt", "Pushups.csv"]
test_resources_path = os.path.dirname(os.getcwd()) + "\\test_resources\\"


def create_paths():
    paths = list()
    for p in possible_paths:
        x = test_resources_path + p
        paths.append(x)
    return paths


def file_exists_and_is_csv(filepath):
    if (
        os.path.isfile(filepath)
        and filepath.casefold().endswith(".csv")
    ):
        return True


class ImporterTest(ut.TestCase):

    def test_path_is_string(self):
        for p in list_strings:
            self.assertIsInstance(fi.Importer(p).filepath, str)
        for n in list_not_strings:
            self.assertIsInstance(fi.Importer(n).filepath, str)

    def test_file_exists(self):
        for p in create_paths():
            f = fi.Importer(p)
            if os.path.isfile(p):
                self.assertTrue(f.file_exists)
            else:
                self.assertFalse(f.file_exists)

    def test_is_csv(self):
        for p in create_paths():
            f = fi.Importer(p)
            if p.endswith(".csv"):
                self.assertTrue(f.file_is_csv)
            else:
                self.assertFalse(f.file_is_csv)

    def test_is_ready(self):
        for p in create_paths():
            f = fi.Importer(p)
            if file_exists_and_is_csv(p):
                self.assertTrue(f.file_is_ready)
            else:
                self.assertFalse(f.file_is_ready)

    def test_data_init_as_none(self):
        for p in create_paths():
            f = fi.Importer(p)
            self.assertIsNone(f.data)



