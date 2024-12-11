print('Đào Quang Huy MSSV 235752021610051')
class StringReversal:
    def __init__(self, input_string: str):
        self.input_string = input_string

    def reverse_words(self) -> str:
        # Tách chuỗi thành danh sách các từ
        words = self.input_string.split()
        
        # Đảo ngược thứ tự các từ trong danh sách
        reversed_words = words[::-1]
        
        # Nối các từ lại thành chuỗi, cách nhau bởi dấu cách
        return ' '.join(reversed_words)


# Test chương trình
if __name__ == "__main__":
    input_string = 'Đào Quang Huy'
    string_reversal = StringReversal(input_string)
    
    # In ra kết quả đảo ngược chuỗi từ từng chữ
    result = string_reversal.reverse_words()
    print(f"Kết quả đảo ngược chuỗi là: '{result}'")
