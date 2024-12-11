print('Đào Quang Huy MSSV 235752021610051')
import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chọn Ngôn Ngữ Lập Trình")

# Tạo biến để lưu trữ lựa chọn
v = tk.IntVar()
v.set(1)  # Mặc định chọn Python

# Danh sách các ngôn ngữ (giá trị, nhãn hiển thị)
languages = [
    (1, "Python"),
    (2, "Perl"),
    (3, "Java"),
    (4, "C++"),
    (5, "C")
]

# Hàm xử lý khi có lựa chọn mới
def ShowChoice():
    print(f"Bạn đã chọn: {languages[v.get()-1][1]}")

# Tạo nhãn hướng dẫn
label = tk.Label(window,
                 text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
                 justify=tk.LEFT,
                 padx=20)
label.pack()

# Tạo các nút radio
for val, language in languages:
    tk.Radiobutton(window,
                  text=language,
                  padx=20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

# Hiển thị cửa sổ
window.mainloop()
