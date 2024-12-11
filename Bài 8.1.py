print('Đào Quang Huy MSSV 235752021610051')
import turtle  # Nhập thư viện Turtle

# Tạo cửa sổ vẽ và thiết lập màu nền
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo đối tượng rùa và thiết lập các thuộc tính
painter = turtle.Turtle()
painter.fillcolor("blue")  # Màu đổ đầy
painter.pencolor("blue")  # Màu bút vẽ
painter.pensize(3)  # Độ dày bút vẽ

# Hàm vẽ hình vuông
def drawsq(t, s):  # t: đối tượng rùa, s: độ dài cạnh
    for i in range(4):
        t.forward(s)  # Di chuyển về phía trước
        t.left(90)  # Rẽ trái 90 độ

# Vẽ hình chính
for i in range(1, 50):
    painter.left(18)  # Rẽ trái 18 độ
    drawsq(painter, 200)  # Vẽ hình vuông với cạnh dài 200
