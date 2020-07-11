import pandas as pd
def write_csv(path,data):
    df = pd.DataFrame.from_dict(d, orient="index")
    df.to_csv(path,header=False)
def check_data_csv(path, data):
    pass
def read_csv(path):
    my_data = pd.read_csv(path)
    print(my_data)
if __name__ == '__main__':
    d = {'a': (1, 101), 'b': (2, 202), 'c': (3, 303)}
    path = 'data.csv'
    write_csv(path,d)
    read_csv(path)
 