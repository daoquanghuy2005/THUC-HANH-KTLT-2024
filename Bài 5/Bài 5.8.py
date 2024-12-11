print('Đào Quang Huy MSSV 235752021610051')
# main.py

import sequential_search

def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập danh sách các phần tử
    dlist = []
    print(f"Nhập {n} phần tử vào danh sách:")
    for i in range(n):
        element = input(f"Phần tử {i+1}: ")
        dlist.append(element)
    
    # Nhập phần tử cần tìm
    item = input("Nhập phần tử cần tìm: ")
    
    # Gọi hàm tìm kiếm tuyến tính
    result = sequential_search.Sequential_Search(dlist, item)
    
    # Hiển thị kết quả tìm kiếm
    if result != -1:
        print(f"Phần tử '{item}' được tìm thấy tại vị trí {result}.")
    else:
        print(f"Phần tử '{item}' không có trong danh sách.")

if __name__ == "__main__":
    main()
