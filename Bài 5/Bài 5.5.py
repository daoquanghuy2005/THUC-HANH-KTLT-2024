print('Đào Quang Huy MSSV 235752021610051')
# main.py

import mymodule

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng các hàm từ mymodule để xử lý
sorted_lst = mymodule.sort_list(lst)  # Sắp xếp danh sách
max_value = mymodule.find_max(lst)    # Tìm phần tử lớn nhất
min_value = mymodule.find_min(lst)    # Tìm phần tử nhỏ nhất

# In kết quả
print("\nDanh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất trong danh sách:", max_value)
print("Phần tử nhỏ nhất trong danh sách:", min_value)
