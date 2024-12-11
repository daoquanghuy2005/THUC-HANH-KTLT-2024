print('Đào Quang Huy MSSV 235752021610051')
def sao_chep_tep(tep_nguon, tep_dich):
    try:
        # Mở tệp nguồn để đọc và tệp đích để ghi
        with open(tep_nguon, 'r', encoding='utf-8') as file_nguon:
            # Đọc toàn bộ nội dung tệp nguồn
            noi_dung = file_nguon.read()
        
        # Mở tệp đích để ghi nội dung
        with open(tep_dich, 'w', encoding='utf-8') as file_dich:
            # Ghi nội dung vào tệp đích
            file_dich.write(noi_dung)
        
        print(f"Đã sao chép nội dung từ tệp {tep_nguon} sang tệp {tep_dich}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
tep_nguon = "source.txt"  # Đường dẫn ( ghi rỗ ổ đĩa, thư mục tên file)
tep_dich = "destination.txt"  # Đường dẫn ( ghi rơ ổ đĩa, thư mục tên file)

sao_chep_tep(tep_nguon, tep_dich)
