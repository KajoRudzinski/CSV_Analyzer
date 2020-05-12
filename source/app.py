"""
Will contain core of the application
For now serves as manual test of end-to-end workflow
"""
import file_io as fi
import os

file = "x.csv"
path = os.path.dirname(os.getcwd()) + "\\test_resources\\"
filepath = path + file


t = fi.Importer(filepath)
t.get_data()
print(t.data)