class HandleListValue:
    def __init__(self, lst_origin):
        self.list_orginal = lst_origin

    def tim_so_chan_trong_list(self):
        rs = []
        for i in self.list_orginal:
            if i % 2 == 0:
                rs.append(i)
        return rs

    def tim_so_le_trong_list(self):
        rs = []
        for i in self.list_orginal:
            if i % 2 != 0:
                rs.append(i)
        return rs

    def tinh_tong_list(self):
        return sum(self.list_orginal)

    def tinh_boi_so_cua_tong(self, x):
        return self.tinh_tong_list()*x


A = [1, 2, 3, 4, 5, 6, 7]

list_handler = HandleListValue(lst_origin=A)

print(list_handler.tim_so_chan_trong_list())
print("==================")
print(list_handler.tim_so_le_trong_list())
print("==================")
print(list_handler.tinh_tong_list())
print("==================")
print(list_handler.tinh_boi_so_cua_tong(x=10))
