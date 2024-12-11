import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn ngôn ngữ lập trình")

# Tạo biến để lưu trữ lựa chọn
v = tk.IntVar()
v.set(1)  # Mặc định chọn Python

# Danh sách các ngôn ngữ
languages = [
    ("Python", 1),
    ("Perl",  2),
    ("Java",  3),
    ("C++",  4),
    ("C",  5)
]

# Hàm xử lý khi có lựa chọn mới
def ShowChoice():
    print(f"Bạn đã chọn: {languages[v.get()-1][1]}")

# Tạo nhãn hướng dẫn
label = tk.Label(root,
                 text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
                 justify=tk.LEFT,
                 padx=20)
label.pack()

# Tạo các nút radio
for val, language in languages:
    tk.Radiobutton(root,
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

# Hiển thị cửa sổ
root.mainloop()
