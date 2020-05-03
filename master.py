import pandas as pd

# testing particular csv file
my_csv = pd.read_csv('Pushups.csv')

my_csv_dim =my_csv.shape


def demo_function(r):
    v = r*2
    return v


print("Info about your csv:")
print()
print("Number of rows: \t" + str(my_csv_dim[0]))
print("Number of columns: \t" + str(my_csv_dim[1]))
print("Number of cells: \t" + str(my_csv.size))
print("-" * 40)

print()
print("List of columns:")
print()
print(my_csv.dtypes)

xx = demo_function(3)
print(xx)