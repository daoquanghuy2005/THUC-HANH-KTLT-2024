print('Đào Quang Huy MSSV 235752021610051')
# Class cơ sở
class Nguoi(object):
    def getGender(self):
        return "Unknown"

# Class Nam kế thừa từ Nguoi
class Nam(Nguoi):
    def getGender(self):
        return "Nam"

# Class Nu kế thừa từ Nguoi
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng từ các lớp con
aNam = Nam()
aNu = Nu()

# In kết quả từ phương thức getGender của các đối tượng
print(aNam.getGender())  # In ra "Nam"
print(aNu.getGender())   # In ra "Nữ"
