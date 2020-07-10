d = dict();
data = {
    "id": "002",
    "name": "Hoang Minh"
}
d.setdefault('sinhvien2',data)
d["sinhvien1"] = {
    "id": "001",
    "name": "Hoang Minh"
}
d.__setitem__('sinhvien3',data);
print(d)