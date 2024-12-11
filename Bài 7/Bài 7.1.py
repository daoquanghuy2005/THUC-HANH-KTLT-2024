print('Đào Quang Huy MSSV 235752021610051')
# Mở file với mã hóa utf-8
with open('D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.1.py', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        reversed_line = line[::-1]
        print(reversed_line)
