import unittest as ut
import file_io as fi
import os as os

possible_paths = [1, True, 0.2, "z", ".csv", ".txt"]


class FileImporterTest(ut.TestCase):

    def test_path_is_string(self):
        for p in possible_paths:
            self.assertIsInstance(fi.FileImporter(p).filepath, str)

    def test_checked_if_file_exists(self):
        for p in possible_paths:
            if os.path.isfile(fi.FileImporter(p).filepath):
                self.assertTrue(fi.FileImporter(p).hasfile)

    def test_checked_if_file_is_csv(self):
        for p in possible_paths:
            if fi.FileImporter(p).filepath.casefold().endswith(".csv"):
                self.assertTrue(fi.FileImporter(p).iscsv)
