import unittest as ut
import file_io as fi
import os as os


class FileImporterTest(ut.TestCase):

    def test_path_is_string(self):
        self.assertIsInstance(fi.FileImporter(1).filepath, str)
        self.assertIsInstance(fi.FileImporter("z").filepath, str)

    def test_checked_if_file_exists(self):
        if os.path.isfile(fi.FileImporter(1).filepath):
            pass
        else:
            self.assertFalse(fi.FileImporter(1).hasfile)

    def test_checked_if_file_is_csv(self):
        if fi.FileImporter(1).filepath.casefold().endswith(".csv"):
            pass
        else:
            self.assertFalse(fi.FileImporter(1).iscsv)

# TODO:
#  use for loop to check different results
#  for differnt filepaths provided (for if in 1, "z", "pushups.csv")