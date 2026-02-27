import turtle 
t = turtle.Turtle()
t.speed(0)
t.width(2)

# pindah ke posisi yang pas
t.penup(); t.goto(-100, 50); t.pendown()

# kreasi bintang pelangi
colors = ["red", "purple", "blue", "green" , "orange", "yellow"]

for i in range(50):
    t.color(colors[i % 6]) # ganti warna otomatis
    t.forward(i * 5)       # panjang garis makin lama makin besar
    t.right(144)           # sudut ajaib pembentuk bintang

turtle.done() 