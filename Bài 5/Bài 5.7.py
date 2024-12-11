print('Đào Quang Huy MSSV 235752021610051')
import numpy as np

# Tạo một mảng có cấu trúc với các cột: Tên, Chiều cao, Lớp
dt = np.dtype([('Tên', 'U50'), ('Chiều cao', 'f4'), ('Lớp', 'U20')])

# Dữ liệu về sinh viên
data = np.array([('Đào Quang Huy', 1.75, '12A1'),
                 ('Ngô Mạnh Nguyên', 1.60, '12B1'),
                 ('Đào Mạnh Nguyên', 1.80, '12A2'),
                 ('Ngô Quang Huy', 1.65, '12C1')], dtype=dt)

# Sắp xếp mảng theo chiều cao (cột 'Chiều cao')
sorted_data = np.sort(data, order='Chiều cao')

# In ra mảng đã sắp xếp
print(sorted_data)
