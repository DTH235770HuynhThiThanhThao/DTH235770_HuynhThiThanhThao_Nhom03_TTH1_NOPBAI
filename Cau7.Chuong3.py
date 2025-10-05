import datetime

# Nhập ngày từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    ngay_hien_tai = datetime.date(nam, thang, ngay)

    # Tính ngày kế tiếp
    ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)

    # In kết quả
    print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))

except ValueError:
    print("Ngày không hợp lệ. Vui lòng nhập lại.")
