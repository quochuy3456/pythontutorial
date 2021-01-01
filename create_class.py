# Viết hàm cộng thêm 1 vào các phần tử trong list


# Viết code tính tài xỉu tử 3 con xúc xác có 6 mặt

# from random import randint
#
# player = str(input("Nhap tai hoac xiu: ")).lower()
# so_tien = int(input("Bao nhieu tien: "))
#
# rd = [randint(1, 6), randint(1, 6), randint(1, 6)]
# _sum = sum(rd)
# print(rd)
# rs = "tai" if _sum >= 10 else "xiu"
#
# if player == rs:
#     print("Win: ", so_tien + 0.7*so_tien)
# else:
#     print("Lose")

A = [10, 2, 3, 4, 5]
#
# B = [x + 1 for x in A]
# print(B)

# import numpy as np
# print(list(np.array(A) + 1))

# print(list(map(lambda x: x+1, A)))

def sum(gsdgsdfs):
    return gsdgsdfs + 1

print(list(map(sum, A)))
