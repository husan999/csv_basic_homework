import csv
def get_first_row(data):
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data = csv.reader(data)
   for i in data:
        return i
# Read the csv file
f=open("data.csv").read()
print(get_first_row(f.split("\n")))


