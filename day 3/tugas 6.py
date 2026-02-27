import turtle
import math

def draw_circle(radius, color, border_color=None, border_width=1):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    if border_color:
        turtle.pencolor(border_color)
        turtle.pensize(border_width)
    
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def write_circular_text(text, radius, start_angle, direction=1):
    # direction 1 untuk atas (normal), -1 untuk bawah (terbalik)
    turtle.penup()
    angle_step = 10  # Jarak antar huruf
    
    for i, char in enumerate(text):
        angle = start_angle - (i * angle_step * direction)
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        turtle.goto(x, y)
        turtle.setheading(angle - 90 if direction == 1 else angle + 90)
        turtle.write(char, align="center", font=("Arial", 14, "bold"))

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

def draw_hand():
    # Sederhanakan bentuk tangan dengan poligon
    turtle.penup()
    turtle.goto(-30, -50)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.pencolor("white")
    turtle.pensize(3)
    turtle.begin_fill()
    
    # Gambar telapak dan jari (versi penyederhanaan)
    turtle.setheading(90)
    turtle.forward(60) # Sisi kiri
    turtle.circle(-10, 180) # Ujung jari telunjuk
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40) # Jari-jari lain
    turtle.right(90)
    turtle.circle(-15, 180)
    turtle.forward(70)
    turtle.goto(-30, -50)
    
    turtle.end_fill()
    
    # Lingkaran "Click" di atas jari
    turtle.penup()
    turtle.goto(-10, 65)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(4)
    turtle.circle(12)

# Konfigurasi Utama
turtle.speed(0)
turtle.hideturtle()
turtle.setup(500, 500)

# 1. Lingkaran luar hitam
draw_circle(180, "black")

# 2. Lingkaran putih (ring teks)
draw_circle(170, "white")

# 3. Lingkaran biru tengah
draw_circle(125, "#1a3a7a") # Biru tua

# 4. Teks Atas
write_circular_text("SEKOLAH MENENGAH KEJURUAN", 140, 155, 1)

# 5. Teks Bawah
write_circular_text("PRESTASI PRIMA", 140, -45, -1)

# 6. Bintang pemisah
draw_star(-155, 0, 15)
draw_star(145, 0, 15)

# 7. Ikon Tangan (Penyederhanaan)
draw_hand()

turtle.done()