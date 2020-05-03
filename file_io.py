import os as os


class FileImporter:
    """Handles importing csv files"""

    def __init__(self, filepath):
        self.filepath = str(filepath)
        self.hasfile = self.file_exists()
        self.iscsv = self.file_is_csv()

    def file_exists(self):
        if os.path.isfile(self.filepath):
            return True

    def file_is_csv(self):
        if self.filepath.casefold().endswith(".csv"):
            return True

