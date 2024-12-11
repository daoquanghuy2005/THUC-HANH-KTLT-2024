print('Đào Quang Huy MSSV 235752021610051')
import os
def doc_n_dong_cuoi(ten_tep, n):
    # Kiểm tra nếu tệp tồn tại
    if not os.path.exists(ten_tep):
        print(f"Tệp {ten_tep} không tồn tại!")
        return []

    with open(ten_tep, 'r', encoding='utf-8') as f:
        dong = f.readlines()
        
        # Nếu tệp có ít dòng hơn n, lấy toàn bộ tệp
        if len(dong) < n:
            print(f"Tệp chỉ có {len(dong)} dòng, lấy tất cả.")
            return dong  # Trả về tất cả các dòng trong tệp
        return dong[-n:]  # Lấy n dòng cuối

# Ví dụ sử dụng
ten_tep = "D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.1.py"
n = 3
dong_cuoi = doc_n_dong_cuoi(ten_tep, n)
if dong_cuoi:
    for dong in dong_cuoi:
        print(dong, end='')  # In các dòng mà không thêm ký tự xuống dòng
