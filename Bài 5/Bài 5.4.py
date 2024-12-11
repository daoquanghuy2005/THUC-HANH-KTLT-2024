print('Đào Quang Huy MSSV 235752021610051')
import numpy as np

# Tạo mảng với các giá trị từ 12 đến 38 (bao gồm cả 12, không bao gồm 38)
arr = np.arange(12, 39)

# Đảo ngược mảng
reversed_arr = arr[::-1]

# In mảng ban đầu và mảng đã đảo ngược ra màn hình
print("Mảng ban đầu:")
print(arr)
print("\nMảng sau khi đảo ngược:")
print(reversed_arr)
