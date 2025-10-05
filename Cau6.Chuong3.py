def doc_so(n):
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 0 or n > 99:
        return "Số không hợp lệ"

    if n < 10:
        return hang_don_vi[n]

    chuc = n // 10
    don_vi = n % 10

    if chuc == 1:
        if don_vi == 0:
            return "mười"
        elif don_vi == 5:
            return "mười lăm"
        else:
            return "mười " + hang_don_vi[don_vi]
    else:
        if don_vi == 0:
            return hang_chuc[chuc]
        elif don_vi == 1:
            return hang_chuc[chuc] + " mốt"
        elif don_vi == 5:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + hang_don_vi[don_vi]

# Ví dụ:
print(doc_so(35))  # ba mươi lăm
print(doc_so(5))   # năm
print(doc_so(21))  # hai mươi mốt
print(doc_so(93))  