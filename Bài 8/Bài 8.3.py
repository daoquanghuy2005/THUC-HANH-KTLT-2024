print('Đào Quang Huy MSSV 235752021610051')
import turtle, random  # Nhập thư viện Turtle và Random

# Danh sách các màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng rùa và thiết lập độ dày bút vẽ
painter = turtle.Turtle()
painter.pensize(3)

# Vẽ nhiều hình tròn với màu sắc ngẫu nhiên
for i in range(20):
    # Chọn màu ngẫu nhiên
    color = random.choice(colors)
    painter.pencolor(color)  # Đặt màu bút vẽ

    # Vẽ hình tròn
    painter.circle(100)

    # Xoay và di chuyển rùa
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)  # Quay về vị trí xuất phát
