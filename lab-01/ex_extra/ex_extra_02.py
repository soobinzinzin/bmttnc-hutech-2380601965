import re


def tinh_tong_so_trong_chuoi(chuoi):
    cac_so = [int(x) for x in re.findall(r'-?\d+', chuoi)]
    tong_duong = sum(x for x in cac_so if x > 0)
    tong_am = sum(x for x in cac_so if x < 0)
    return tong_duong, tong_am


chuoi_nhap = input("Nhap chuoi can tinh tong cac so: ")
duong, am = tinh_tong_so_trong_chuoi(chuoi_nhap)
print(f"Gia tri duong: {duong}. Gia tri am: {am}.")
