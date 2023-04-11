import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data=csv.reader(data)
    ls=[]
    for i in data:
        if len(i)!=0:
            ls.append(i)
    return len(ls)
# Read the csv file
f = open("data.csv").read()
print(find_number_of_columns(f.split('\n')))
