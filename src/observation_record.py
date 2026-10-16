from datetime import datetime

ma_quan_sat = input("Nhập mã quan sát: ")
ten_dai_luong = input("Nhập tên đại lượng: ")
gia_tri_do = float(input("Nhập giá trị đo: "))
don_vi = input("Nhập đơn vị: ")

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng : {ten_dai_luong}")
print(f"Giá trị : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm : {thoi_diem_text}")
