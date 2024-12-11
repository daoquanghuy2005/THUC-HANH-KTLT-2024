print('Đào Quang Huy MSSV 235752021610051')
def tinh_so_du(nhat_ky):
  """Tính số dư tài khoản dựa trên nhật ký giao dịch

  Args:
    nhat_ky: Danh sách các giao dịch (D: gửi, W: rút)

  Returns:
    int: Số dư cuối cùng của tài khoản
  """

  so_du = 0  # Khởi tạo số dư ban đầu là 0
  for giao_dich in nhat_ky:  # Duyệt qua từng giao dịch trong nhật ký
    loai_giao_dich, so_tien = giao_dich.split()  # Tách loại giao dịch và số tiền
    so_tien = int(so_tien)  # Chuyển số tiền thành số nguyên
    if loai_giao_dich == 'D':  # Nếu là giao dịch gửi tiền
      so_du += so_tien  # Thêm số tiền vào số dư
    elif loai_giao_dich == 'W':  # Nếu là giao dịch rút tiền
      so_du -= so_tien  # Trừ số tiền khỏi số dư
  return so_du  # Trả về số dư cuối cùng

# Nhập nhật ký giao dịch từ người dùng
nhat_ky = []  # Khởi tạo danh sách nhật ký giao dịch
while True:
  giao_dich = input("Nhập giao dịch (D <số tiền> hoặc W <số tiền>, nhập 'quit' để kết thúc): ")
  if giao_dich.lower() == 'quit':  # Nếu người dùng nhập 'quit', thoát vòng lặp
    break
  nhat_ky.append(giao_dich)  # Thêm giao dịch vào danh sách nhật ký

# Tính số dư và in kết quả
so_du_cuoi = tinh_so_du(nhat_ky)  # Gọi hàm tính số dư cuối cùng
print("Số dư cuối cùng của tài khoản:", so_du_cuoi)  # In số dư cuối cùng
