#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data=csv.reader(data)
    x=[]
    for i in data:
        if len(i)!=0:
            x.append(i[1:2])
    return x
    
# Read the csv file
f= open("data.csv").read()
print(get_column_names(f.split("\n")))