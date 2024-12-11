print('Đào Quang Huy MSSV 235752021610051')
import binary_search  # Import module chứa hàm tìm kiếm nhị phân

def main():
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử
    lst = []
    print("Nhập các phần tử:")
    for i in range(n):
        lst.append(int(input(f"Phần tử {i + 1}: ")))
    
    # Sắp xếp danh sách
    lst.sort()
    
    # Nhập giá trị cần tìm
    value = int(input("Nhập giá trị cần tìm: "))
    
    # Sử dụng hàm binary_search từ module binary_search
    result = binary_search.binary_search(lst, value)
    
    # In kết quả
    if result != -1:
        print(f"Giá trị {value} được tìm thấy tại chỉ mục {result}.")
    else:
        print(f"Giá trị {value} không có trong danh sách.")

# Chạy chương trình chính
if __name__ == "__main__":
    main()
