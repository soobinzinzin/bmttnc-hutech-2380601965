import itertools

danh_sach = [1, 2, 3]
hoan_vi = list(itertools.permutations(danh_sach))

print("Tat ca cac hoan vi cua [1, 2, 3]:")
for hv in hoan_vi:
    print(hv)
