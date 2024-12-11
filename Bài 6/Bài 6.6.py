print('Đào Quang Huy MSSV 235752021610051')
class StringProcessor:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        # Nhận chuỗi từ người dùng
        self.user_string = input("Nhập một chuỗi: ")

    def print_String(self):
        # In chuỗi với chữ in hoa
        print(self.user_string.upper())

# Test chương trình
if __name__ == "__main__":
    string_processor = StringProcessor()
    
    # Lấy chuỗi từ người dùng
    string_processor.get_String()
    
    # In chuỗi đó bằng chữ in hoa
    string_processor.print_String()
