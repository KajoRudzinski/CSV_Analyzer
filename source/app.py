"""
Will contain core of the application
For now serves as manual test of end-to-end workflow
"""
possible_paths = ["z", "empty_csv.csv", ".txt", "Pushups.csv"]

# the only remaining problem is to read an empty file

import file_io as fi
import os

file = "empty_csv.csv"
path = os.path.dirname(os.getcwd()) + "\\test_resources\\"
filepath = path + file


t = fi.Importer(filepath)
t.get_data()
if t.output is None:
    print(t.error)