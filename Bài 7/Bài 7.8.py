print('Đào Quang Huy MSSV 235752021610051')
def ghi_danh_sach_vao_tep(ten_tep, danh_sach):
    try:
        # Mở tệp ở chế độ ghi (write) với mã hóa utf-8
        with open(ten_tep, 'w', encoding='utf-8') as file:
            for item in danh_sach:
                # Ghi từng phần tử của danh sách vào tệp, mỗi phần tử trên một dòng
                file.write(str(item) + '\n')
        print(f"Đã ghi nội dung danh sách vào tệp {ten_tep}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
danh_sach = ["Đào", "Quang", "Huy", "2005"]
ten_tep = "D:\Thực hành lập trình\Bài 7 Thao tác trên tập tin và thư mục trong Python\Câu 7.1.py"  # Đường dẫn của tệp cần ghi

ghi_danh_sach_vao_tep(ten_tep, danh_sach)
