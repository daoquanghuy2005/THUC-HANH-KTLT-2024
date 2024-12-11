print('Đào Quang Huy MSSV 235752021610051')
import tkinter as tk

def click_button():
    # Đây là hàm sẽ được gọi khi nút bấm được nhấn
    print("Bấm vừa thôi cha ")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Cửa sổ Đơn Giản")

# Tạo nút bấm
button = tk.Button(window, text="Nhấn vào đây", command=click_button)
button.pack()

# Hiển thị cửa sổ
window.mainloop()
