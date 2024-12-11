print('Đào Quang Huy MSSV 235752021610051')
def tim_tu_dai_nhat(van_ban):
    # Tách văn bản thành các từ (sử dụng split để tách theo khoảng trắng)
    tu_list = van_ban.split()
    
    # Tìm độ dài của từ dài nhất
    max_length = max(len(tu) for tu in tu_list)
    
    # Lọc ra những từ có độ dài bằng với độ dài dài nhất
    tu_dai_nhat = [tu for tu in tu_list if len(tu) == max_length]
    
    return tu_dai_nhat

# Ví dụ sử dụng
van_ban = "Đào Quang Huy"
tu_dai_nhat = tim_tu_dai_nhat(van_ban)

print("Những từ dài nhất trong văn bản là:")
for tu in tu_dai_nhat:
    print(tu)
