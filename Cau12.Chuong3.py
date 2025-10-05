for i in range(1, 11):         # Duyệt từ 1 đến 10 (số nhân)
    for j in range(2, 10):     # Duyệt từ 2 đến 9 (số bị nhân)
        line = "{0} * {1:>2} = {2:>2}".format(j, i, j * i)
        print(line, end='\t')  # In trên cùng một dòng, cách nhau bằng tab
    print()                    # Xuống dòng sau mỗi hàng

