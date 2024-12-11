import numpy as np

# Tạo mảng ID sinh viên và chiều cao
student_ids = np.array([101, 102, 103, 104, 105])
heights = np.array([170, 160, 165, 175, 168])

# Sử dụng lexsort để sắp xếp theo chiều cao (chỉ số tăng dần)
sorted_indices = np.lexsort((heights,))  

# In các chỉ số sắp xếp
print("Chỉ số sắp xếp (theo chiều cao):", sorted_indices)

# Dữ liệu sau khi sắp xếp theo chiều cao
sorted_student_ids = student_ids[sorted_indices]
sorted_heights = heights[sorted_indices]

# In kết quả sắp xếp
print("Dữ liệu sau khi sắp xếp:")
for id, height in zip(sorted_student_ids, sorted_heights):
    print(f"ID: {id}, Chiều cao: {height} cm")
