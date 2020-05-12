import os as os
import pandas as pd


class Importer:

    def __init__(self, filepath):
        self.filepath = str(filepath)
        self.name = "Importer"
        self.data = None
        self.file_has_no_data = None
        self.file_exists = os.path.isfile(str(filepath))
        self.file_is_csv = str(filepath).casefold().endswith(".csv")
        self.file_is_ready = self.file_exists and self.file_is_csv

    # works! :D
    # TODO: now work with self.file_has_no_data = None
    def get_data(self):
        if self.file_is_ready:
            self.data = pd.read_csv(self.filepath)
        elif not self.file_exists:
            print("file doesn't exist")
        else:
            # TODO: both statements to be passed as errors somehow
            print("file is not a csv")



#
# class Error:
#
#     def __init__(self, errorname):
#         self.name = errorname
