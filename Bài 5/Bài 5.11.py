import numpy as np

# Tạo mảng có cấu trúc với các trường tên, chiều cao và lớp
data_type = np.dtype([('name', 'U50'), ('height', 'f4'), ('class', 'U20')])

# Tạo mảng dữ liệu
students = np.array([('Đào Quang Huy', 180, '12A'),
                     ('Ngô Mạnh Nguyên', 160, '11B'),
                     ('Nguyễn Hữu Kiều', 165, '12A'),
                     ('Nguyễn Thái Huy', 175, '11B'),
                     ('Lê Văn Hoàng', 168, '12B')],
                    dtype=data_type)

# Sắp xếp theo lớp trước, sau đó theo chiều cao nếu lớp giống nhau
sorted_students = np.sort(students, order=['class', 'height'])

# In kết quả
for student in sorted_students:
    print(f"Tên: {student['name']}, Chiều cao: {student['height']} cm, Lớp: {student['class']}")
