import unittest as ut
import file_io as fi


class FileImporterTest(ut.TestCase):

    def test_if_class_exist(self):
        fi.FileImporter(1)

    def test_if_path_only_accepts_string(self):
        with self.assertRaises(TypeError):
            fi.FileImporter(1)
