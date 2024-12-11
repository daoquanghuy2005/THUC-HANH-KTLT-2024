print('Đào Quang Huy MSSv 235752021610051')
class Circle(object):
    def __init__(self, r):
        """Constructor nhận vào bán kính của hình tròn."""
        self.radius = r
    
    def area(self):
        """Method tính diện tích hình tròn."""
        return self.radius**2 * 3.14

# Tạo đối tượng Circle với bán kính là 2
aCircle = Circle(8)

# In diện tích của hình tròn
print(aCircle.area())
