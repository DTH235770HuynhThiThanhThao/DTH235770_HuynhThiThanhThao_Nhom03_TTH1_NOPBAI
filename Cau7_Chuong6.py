def NhapDaySoTangDan():
    print("\n--- Câu 7: Nhập Dãy Số Tăng Dần ---")
    day_so = []
    
    # Số cuối cùng đã nhập, khởi tạo bằng âm vô cực để số đầu tiên luôn hợp lệ
    so_truoc = float('-inf')

    print("Bắt đầu nhập dãy số (Nhập 'done' để kết thúc):")

    while True:
        try:
            nhap = input(f"Nhập số tiếp theo (lớn hơn {day_so[-1] if day_so else 'số trước'}): ")
            
            if nhap.lower() == 'done':
                break

            so_hien_tai = int(nhap)
            
            # Kiểm tra quy tắc tăng dần
            if so_hien_tai < so_truoc:
                print(f"LỖI: Số {so_hien_tai} KHÔNG lớn hơn số trước ({so_truoc}). Vui lòng nhập lại!")
                continue # Quay lại đầu vòng lặp

            # Nếu hợp lệ, thêm vào dãy và cập nhật so_truoc
            day_so.append(so_hien_tai)
            so_truoc = so_hien_tai

        except ValueError:
            print("LỖI: Vui lòng nhập một số nguyên hợp lệ hoặc 'done'.")
        
    print("-" * 30)
    print("Dãy số đã nhập theo thứ tự tăng dần là:")
    print(day_so)

# Chạy hàm
# NhapDaySoTangDan()