print('Đào Quang Huy MSSV 235752021610051')
class RomanToInteger:
    def __init__(self):
        # Mappings of Roman numerals to integer values
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman: str) -> int:
        # Kết quả ban đầu là 0
        result = 0
        # Duyệt qua các ký tự trong chuỗi La Mã
        for i in range(len(roman)):
            # Lấy giá trị của ký tự hiện tại
            current_value = self.roman_map[roman[i]]
            
            # Kiểm tra nếu ký tự hiện tại có giá trị nhỏ hơn ký tự tiếp theo
            # thì trừ đi giá trị của ký tự hiện tại, nếu không cộng vào
            if i + 1 < len(roman) and current_value < self.roman_map[roman[i + 1]]:
                result -= current_value
            else:
                result += current_value
                
        return result


# Test chương trình
if __name__ == "__main__":
    roman_converter = RomanToInteger()
    
    # Thử nghiệm với một số La Mã
    roman_numeral = "XVI"
    print(f"Số La Mã {roman_numeral} chuyển thành số nguyên là: {roman_converter.convert(roman_numeral)}")
    
    roman_numeral = "MMV"
    print(f"Số La Mã {roman_numeral} chuyển thành số nguyên là: {roman_converter.convert(roman_numeral)}")
