import operator
import math
import cmath
# truy cập phần tử mảng
lst = [1,2,3,4]
lst[1:] # [2, 3, 4]
lst[:3] # [1, 2, 3]
lst[::2] # [1, 3]
lst[::-1] # [4, 3, 2, 1]
lst[-1:0:-1] # [4, 3, 2]
lst[5:8] # [] since starting index is greater than length of lst, returns empty list
lst[1:10] # [2, 3, 4] same as omitting ending index
# phép toán các số
num = operator.add(2,3)
num = math.sqrt(45)
num = cmath.sqrt(34)
