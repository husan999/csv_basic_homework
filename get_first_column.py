import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data=csv.reader(data)
    x=[]
    for i in data:
        x.append(i[0])
    return x
    
# Read the csv file
f=open("data.csv")
print(get_first_column(f))

