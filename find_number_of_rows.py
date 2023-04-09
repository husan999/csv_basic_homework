import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    data= csv.reader(data)
    for i in data:
        return len(i)
 # Read the csv file
f=open("data.csv").read()
print(find_number_of_rows(f.split()))