print('Đào Quang Huy MSSV 235752021610051')
import math

class Circle:
    def __init__(self, radius):
        # Khởi tạo bán kính của hình tròn
        self.radius = radius

    def area(self):
        # Tính diện tích của hình tròn: A = π * r^2
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Tính chu vi của hình tròn: P = 2 * π * r
        return 2 * math.pi * self.radius

# Test chương trình
if __name__ == "__main__":
    # Nhập bán kính từ người dùng
    radius = float(input("Nhập bán kính của hình tròn: "))
    
    # Tạo đối tượng hình tròn
    circle = Circle(radius)
    
    # In diện tích và chu vi của hình tròn
    print(f"Diện tích của hình tròn là: {circle.area():.2f}")
    print(f"Chu vi của hình tròn là: {circle.perimeter():.2f}")
