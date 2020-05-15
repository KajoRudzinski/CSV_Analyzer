import os as os
import pandas as pd

no_file = "File does not exist"
empty_or_corrupt_file = "Empty or currupt file"
not_csv = "File is not a csv"


class Importer:
    """Imports csv. In case of failure produce an error."""

    def __init__(self, filepath):
        self.filepath = str(filepath)
        self.file_exists = os.path.isfile(str(filepath))
        self.file_is_csv = str(filepath).casefold().endswith(".csv")
        self.file_is_ready = self.file_exists and self.file_is_csv
        self.output = None
        self.error = None

    def get_data(self):
        if self.file_is_ready:
            try:
                self.read_data()
            except Exception:   # TODO: narrow down the exception
                self.get_file_error()

    def read_data(self):
        self.output = pd.read_csv(self.filepath)

    def get_file_error(self):
        if self.file_is_ready:
            self.error = empty_or_corrupt_file
        else:
            if not self.file_exists:
                self.error = no_file
            else:
                self.error = not_csv



