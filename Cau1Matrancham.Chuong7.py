import turtle

t = turtle.Turtle()
#t.hideturtle() ẩn biểu tượng con rùa
t.speed(0)         # tốc độ vẽ nhanh nhất
t.penup()
t.color("blue")    # màu chấm

# Cấu hình ma trận
rows = 7         # số hàng
cols = 5         # số cột
dot_size = 10      # kích thước mỗi dấu chấm
spacing = 30       # khoảng cách giữa các chấm

# Vẽ ma trận chấm
for y in range(rows):
    for x in range(cols):
        t.goto(x * spacing, -y * spacing)  # vị trí chấm
        t.dot(dot_size)
        
turtle.done()
