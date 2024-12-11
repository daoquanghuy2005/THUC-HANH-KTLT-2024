print('Đào Quang Huy MSSV 235752021610051')
# File: main.py

import mymath

# Danh sách các giá trị
values = [2, 4, 6, 8, 10]

# Tính bình phương của từng giá trị trong danh sách
print('Squares:')
for v in values:
    print(mymath.square(v))  # Gọi hàm square từ mymath

# Tính lập phương của từng giá trị trong danh sách
print('Cubes:')
for v in values:
    print(mymath.cube(v))  # Gọi hàm cube từ mymath

# Tính trung bình của danh sách
print('Average: ' + str(mymath.average(values)))  # Gọi hàm average từ mymath

