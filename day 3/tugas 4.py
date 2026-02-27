import turtle 
t = turtle.Turtle()
t.speed(0)
t.left(90) # arahkan turtle ke atas (batang pohon)

def pohon(cabang):
    if cabang > 5:
        t.forward(cabang)
        t.right(20)
        pohon(cabang - 15) # cabang kanan
        t.left(40)
        pohon(cabang - 15) # cabang kiri
        t.right(20)
        t.backward(cabang)

t.penup(); t.goto(0, -200); t.pendown()
pohon(75) # angka 75 adalah panjang batang utama
turtle.done()