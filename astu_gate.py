from cs1graphics import *
import time 
import threading
# from PIL import Image

canvas = Canvas(1350, 700)
canvas.setTitle("ASTU Gate Project")
canvas.setBackgroundColor("sky blue")

x = Path(Point(0, 450), Point(1350, 450))
x.setBorderWidth(5)
x.setDepth(40)
canvas.add(x)

y = Path(Point(675, 0), Point(675, 700))
y.setBorderWidth(5)
y.setDepth(40)
canvas.add(y)

def scale():
    x = 50
    y = 50
    for i in range(27):
        canvas.add(Path(Point(x, 0), Point(x, 700)))
        x += 50

    for i in range(14):
        canvas.add(Path(Point(0, y), Point(1370, y)))
        y += 50

def geda_gate():
    geda_gate = Layer()

    color = (192, 202, 183)
    color1 = (87, 87, 86)
    circle1 = Circle(300)
    circle1.moveTo(700, 500)
    circle1.setFillColor(color1)
    circle1.setBorderWidth(15)
    circle1.setBorderColor(color)


    circle2 = Circle(250)
    circle2.moveTo(550, 500)
    circle2.setFillColor(color1)
    circle2.setBorderWidth(12)
    circle2.setBorderColor(color)

    circle3 = Circle(150)
    circle3.moveTo(350, 500)
    circle3.setFillColor("orange")
    circle3.setDepth(60)
    circle3.setBorderWidth(8)
    circle3.setBorderColor(color)

    circle4 = Circle(200)
    circle4.moveTo(1010, 500)
    circle4.setFillColor("orange")
    circle4.setDepth(60)
    circle4.setBorderWidth(10)
    circle4.setBorderColor(color)

    line1 = Path(Point(785, 425), Point(915, 280))
    line1.setBorderWidth(15)
    line1.setBorderColor(color)

    line2 = Path(Point(777, 400), Point(870, 250))
    line2.setBorderWidth(15)
    line2.setBorderColor(color)

    line3 = Path(Point(760, 370), Point(820, 230))
    line3.setBorderWidth(15)
    line3.setBorderColor(color)

    line4 = Path(Point(742, 343), Point(775, 205))
    line4.setBorderWidth(15)
    line4.setBorderColor(color)

    line5 = Path(Point(722, 323), Point(725, 205))
    line5.setBorderWidth(13)
    line5.setBorderColor(color)

    line5 = Path(Point(722, 320), Point(725, 205))
    line5.setBorderWidth(13)
    line5.setBorderColor(color)

    line6 = Path(Point(700, 303), Point(680, 205))
    line6.setBorderWidth(13)
    line6.setBorderColor(color)

    line7 = Path(Point(670, 282), Point(635, 205))
    line7.setBorderWidth(13)
    line7.setBorderColor(color)

    line8 = Path(Point(630, 265), Point(590, 215))
    line8.setBorderWidth(13)
    line8.setBorderColor(color)

    cover = Rectangle(1020, 350)
    cover.setFillColor("sky blue")
    cover.setBorderColor("transparent")
    cover.moveTo(705, 675)
    cover.setDepth(40)

    geda_gate.add(circle1)
    geda_gate.add(circle2)
    geda_gate.add(circle3)
    geda_gate.add(circle4)
    geda_gate.add(line1)
    geda_gate.add(line2)
    geda_gate.add(line3)
    geda_gate.add(line4)
    geda_gate.add(line5)
    geda_gate.add(line6)
    geda_gate.add(line7)
    geda_gate.add(line8)
    geda_gate.add(cover)

    geda_gate.moveTo(900, 275)
    canvas.add(geda_gate)

    geda_gate.scale(0.35)
    



def main_gate():
    main_gate = Layer()

    ellipse = Ellipse(1200, 450)
    ellipse.moveTo(675, 500)
    ellipse.setBorderColor("blue")
    ellipse.setFillColor("white")
    ellipse.setDepth(60)
    
    ellipse.setBorderWidth(15)
    # ellipse.setFillColor("trasnpalent")

    color = (87, 87, 86)
    circle1 = Circle(60)
    circle1.setBorderWidth(8)
    circle1.setBorderColor("blue")
    circle1.move(350, 450)
    circle1.setFillColor(color)
    circle1.setDepth(60)

    circle2 = Circle(100)
    circle2.setBorderWidth(8)
    circle2.setBorderColor("blue")
    circle2.move(550, 450)
    circle2.setFillColor(color)
    circle2.setDepth(60)

    circle3 = Circle(100)
    circle3.setBorderWidth(8)
    circle3.setBorderColor("blue")
    circle3.move(800, 450)
    circle3.setFillColor(color)
    circle3.setDepth(60)

    circle4 = Circle(60)
    circle4.setBorderWidth(8)
    circle4.setBorderColor("blue")
    circle4.move(1000, 450)
    circle4.setFillColor(color)
    circle4.setDepth(60)

    a = Text("A", 40)
    a.moveTo(460, 350)
    a.setFontColor("blue")

    s = Text("S", 40)
    s.moveTo(600, 320)
    s.setFontColor("blue")

    t = Text("T", 40)
    t.moveTo(750, 320)
    t.setFontColor("blue")

    u = Text("U", 40)
    u.moveTo(890, 350)
    u.setFontColor("blue")

    # img = Image.open(r"E:\logo.png")
    # img.show()
    # image = Image(r"E:\logo.png")

    cover = Rectangle(1250, 320)
    cover.setFillColor("sky blue")
    cover.moveTo(675, 595)
    cover.setBorderColor("transparent")

    road = Polygon(Point(230, 700), Point(1130, 700), Point(950, 50), Point(400, 50))
    road.setBorderColor("black")
    road.setBorderWidth(5)
    # road.setFillColor((47, 74, 78))
    road.setDepth(600)

    main_gate.add(ellipse)
    main_gate.add(circle1)
    main_gate.add(circle2)
    main_gate.add(circle3)
    main_gate.add(circle4)
    main_gate.add(a)
    main_gate.add(s)
    main_gate.add(t)
    main_gate.add(u)
    main_gate.add(cover)
    # main_gate.add(road)

    main_gate.moveTo(5, 300)
    canvas.add(main_gate)
    main_gate.scale(0.35)

def road():
    color = (87, 87, 86)
    road1 = Polygon(Point(375, 450), Point(100, 450), Point(200,100), Point(1125, 100), Point(1250, 450), Point(1000, 450), Point(1050, 150), Point(275, 150))
    road1.setFillColor(color)
    road1.setDepth(700)
    canvas.add(road1)

    road2 = Polygon(Point(0, 450), Point(1350, 450), Point(1350, 550), Point(0, 550))
    road2.setFillColor(color)
    road2.setDepth(40)
    canvas.add(road2)

def green_area():
    green = Polygon(Point(375, 450), Point(275, 150), Point(1050, 150), Point(1000, 450))
    green.setFillColor((19, 133, 16))
    green.setDepth(70)
    canvas.add(green)

def fence():
    line1 = Polygon(Point(400, 450), Point(970, 450), Point(970, 430), Point(400, 430))
    line1.setBorderWidth(10)
    line1.setFillColor("black")
    line1.setDepth(70)

    line2 = Path(Point(400, 420), Point(975, 420))
    line2.setBorderColor("red")
    line2.setDepth(40)

    
    line3 = Path(Point(400, 410), Point(975, 410))
    line3.setBorderColor("red")
    line3.setDepth(40)

    
    line4 = Path(Point(400, 400), Point(975, 400))
    line4.setBorderColor("red")
    line4.setDepth(40)

    color = (19, 133, 16)

    rec = Layer()
    rec.setDepth(20)

    rec1 = Polygon(Point(485, 450), Point(515, 450), Point(515, 380), Point(485, 380))
    rec1.setFillColor(color)
    rec1.setBorderColor("red")
    rec1.setBorderWidth(5)
    rec.add(rec1)

    rib1 = Path(Point(495, 450), Point(495, 380))
    rib1.setBorderColor("red")
    rec.add(rib1)

    rib2 = Path(Point(505, 450), Point(505, 380))
    rib2.setBorderColor("red")
    rec.add(rib2)

    rec2 = rec.clone()
    rec2.moveTo(130, 0)
    canvas.add(rec2)

    rec3 = rec2.clone()
    rec3.moveTo(260, 0)
    canvas.add(rec3)

    rec4 = rec3.clone()
    rec4.moveTo(390, 0)
    canvas.add(rec4)


    canvas.add(line1)
    canvas.add(line2)
    canvas.add(line3)
    canvas.add(line4)

    canvas.add(rec)
    
    
    


geda_gate()
main_gate()
# scale()
road()
green_area()
fence()