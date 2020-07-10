def printId(id):
    print(id)
class students:
    def __init__(self,id,name,mark):
        self.id = id
        self.name = name
        self.mark = mark
    def __getitem__(self,id):
        return id
minhanh = students('001','minh anh',23)
if __name__ == '__main__':
    printId(323)
