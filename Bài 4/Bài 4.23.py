print('Đào Quang Huy MSSV 235752021610051')
def dem_chu_cai_va_chu_so(cau):
  """Đếm số chữ cái và chữ số trong một câu

  Args:
    cau: Câu cần đếm

  Returns:
    tuple: Một tuple chứa (số chữ cái, số chữ số)
  """

  so_chu_cai = 0  # Biến lưu số lượng chữ cái
  so_chu_so = 0   # Biến lưu số lượng chữ số

  for ky_tu in cau:  # Duyệt qua từng ký tự trong câu
    if ky_tu.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái không
      so_chu_cai += 1  # Nếu là chữ cái, tăng số chữ cái lên 1
    elif ky_tu.isdigit():  # Kiểm tra xem ký tự có phải là chữ số không
      so_chu_so += 1  # Nếu là chữ số, tăng số chữ số lên 1

  return so_chu_cai, so_chu_so  # Trả về tuple chứa số chữ cái và chữ số

# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

# Gọi hàm đếm và in kết quả
so_chu_cai, so_chu_so = dem_chu_cai_va_chu_so(cau)
print("Số chữ cái là:", so_chu_cai)
print("Số chữ số là:", so_chu_so)
