import turtle

t = turtle.Turtle()

def kotak(warna, y):
    t.penup(); t.goto(-100, y); t.pendown()
    t.color("black", warna); t.begin_fill()
    for _ in range(2):
        t.forward(200); t.right(50) # panjang 200, lebar 50
        t.right(40); t.forward(50); t.right(90)
    t.end_fill()

# gambar bagian merah (atas)
kotak("red", 50)
# gambar bagian putih (bawah)
kotak("white", 0)