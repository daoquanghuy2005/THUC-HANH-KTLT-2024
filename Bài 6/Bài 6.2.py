class Hinhchunhat:
  def __init__(self, chieudai, chieurong):
    """Khởi tạo một hình chữ nhật mới.

    Args:
      chieudai: Chiều dài của hình chữ nhật.
      chieurong: Chiều rộng của hình chữ nhật.
    """
    self.chieudai = chieudai
    self.chieurong = chieurong

  def tinh_dien_tich(self):
    """Tính diện tích hình chữ nhật.

    Returns:
      Diện tích của hình chữ nhật.
    """
    return self.chieudai * self.chieurong
# Tạo một hình chữ nhật có chiều dài 5 và chiều rộng 3
hinh_chu_nhat = Hinhchunhat(16, 8)

# Tính diện tích và in kết quả
dien_tich = hinh_chu_nhat.tinh_dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich)
