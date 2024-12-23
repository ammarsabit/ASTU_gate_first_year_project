from cs1graphics import *
import time 
import threading

canvas = Canvas(1350, 550)
canvas.setTitle("ASTU Gate Project")
canvas.setBackgroundColor("sky blue")

def scale():
    x = 50
    y = 50
    for i in range(27):
        x_axis = Path(Point(x, 0), Point(x, 700))
        x_axis.setDepth(10)
        canvas.add(x_axis)
        x += 50

    for i in range(14):
        y_axis = Path(Point(0, y), Point(1370, y))
        y_axis.setDepth(10)
        canvas.add(y_axis)
        y += 50

def geda_gate():
    geda_gate = Layer()

    color =  (192, 202, 183)
    color1 =  (87, 87, 86)
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

    cover = Rectangle(1250, 320)
    cover.setFillColor("sky blue")
    cover.moveTo(675, 595)
    cover.setBorderColor("transparent")

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

    main_gate.moveTo(5, 300)
    canvas.add(main_gate)
    main_gate.scale(0.35)

def text():
    text = Layer()
    text.setDepth(30)

    text1 = Text("ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY", 20)
    text2 = Text("UNIVERSIITII SAAYINSII FI TEKNOLOOGII ADAAMAA", 20)

    text1.setFontColor("blue")
    text2.setFontColor("blue")

    text.add(text1)
    text.add(text2)

    text1.moveTo(685, 220)
    text2.moveTo(685, 250)

    canvas.add(text)

    text.moveTo(5, 299)
    
    text.scale(0.35)

def road():
    color = (87, 87, 86)
    road1 = Polygon(Point(375, 450), Point(100, 450), Point(200,100), Point(1125, 100), Point(1250, 450), Point(1000, 450), Point(1050, 150), Point(275, 150))
    road1.setFillColor(color)
    road1.setDepth(700)
    canvas.add(road1)

    road2 = Polygon(Point(0, 450), Point(1350, 450), Point(1350, 550), Point(0, 550))
    road2.setFillColor(color)
    road2.setBorderColor("transparent")
    road2.setDepth(40)
    canvas.add(road2)

    road3 = Polygon(Point(380, 450), Point(100, 450), Point(40, 700), Point(460, 700))
    road3   .setFillColor(color)
    road3.setDepth(42)
    canvas.add(road3)

def road_lane1():
    lane1 = Path(Point(125, 500), Point(175, 500))
    lane1.setBorderColor("white")
    lane1.setBorderWidth(5)
    lane1.setDepth(35)
    canvas.add(lane1)

    lane2 = lane1.clone()
    lane2.moveTo(225, 500)
    canvas.add(lane2)

    lane3 = lane1.clone()
    lane3.moveTo(325, 500)
    canvas.add(lane3)

    lane4 = lane1.clone()
    lane4.moveTo(500, 500)
    canvas.add(lane4)

    lane5 = lane1.clone()
    lane5.moveTo(625, 500)
    canvas.add(lane5)

    lane6 = lane1.clone()
    lane6.moveTo(750, 500)
    canvas.add(lane6)

    lane7 = lane1.clone()
    lane7.moveTo(900, 500)
    canvas.add(lane7)
    
    lane11 = lane1.clone()
    lane11.moveTo(1075, 500)
    canvas.add(lane11)

    lane12 = lane1.clone()
    lane12.moveTo(1175, 500)
    canvas.add(lane12)

def road_lane2():
    lane1 = Path(Point(225, 200), Point(225, 225))
    lane1.setBorderColor("white")
    lane1.setBorderWidth(5)
    lane1.setDepth(35)
    canvas.add(lane1)

    lane2 = lane1.clone()
    lane2.moveTo(225, 275)
    canvas.add(lane2)

    lane3 = lane1.clone()
    lane3.moveTo(225, 350)
    canvas.add(lane3)

    lane4 = lane1.clone()
    lane4.moveTo(225, 650)
    canvas.add(lane4)

    lane5 = lane1.clone()
    lane5.moveTo(225, 550)
    canvas.add(lane5)

def road_lane3():
    lane1 = Path(Point(1100, 200), Point(1100, 225))
    lane1.setBorderColor("white")
    lane1.setBorderWidth(5)
    lane1.setDepth(35)
    canvas.add(lane1)

    lane2 = lane1.clone()
    lane2.moveTo(1100, 275)
    canvas.add(lane2)

    lane3 = lane2.clone()
    lane3.moveTo(1100   , 350)
    canvas.add(lane3)

def road_lane4():
    lane1 = Path(Point(350, 125), Point(375, 125))
    lane1.setBorderColor("white")
    lane1.setBorderWidth(3)
    lane1.setDepth(35)
    canvas.add(lane1)

    lane2 = lane1.clone()
    lane2.moveTo(425, 125)
    canvas.add(lane2)

    lane3 = lane2.clone()
    lane3.moveTo(525, 125)
    canvas.add(lane3)

    lane4 = lane3.clone()
    lane4.moveTo(625, 125)
    canvas.add(lane4)

    lane5 = lane4.clone()
    lane5.moveTo(725, 125)
    canvas.add(lane5)

    lane6 = lane5.clone()
    lane6.moveTo(825, 125)
    canvas.add(lane6)
    
    lane7 = lane6.clone()
    lane7.moveTo(925, 125)
    canvas.add(lane7)

def zebra():
    zebra1 = Layer()
    zebra1.setDepth(35)

    line1 = Path(Point(50, 460), Point(100, 460))
    line1.setBorderWidth(10)
    line1.setBorderColor("white")
    zebra1.add(line1)
    
    line2 = line1.clone()
    line2.moveTo(50, 480)
    zebra1.add(line2)

    line3 = line2.clone()
    line3.moveTo(50, 500)
    zebra1.add(line3)

    line4 = line3.clone()
    line4.moveTo(50, 520)
    zebra1.add(line4)

    line5 = line4.clone()
    line5.moveTo(50, 540)
    zebra1.add(line5)

    canvas.add(zebra1)

    zebra2 = zebra1.clone()
    zebra2.moveTo(350, 0)
    canvas.add(zebra2)

    zebra3 = zebra1.clone()
    zebra3.moveTo(950, 0)
    canvas.add(zebra3)

    zebra4 = zebra1.clone()
    zebra4.moveTo(1200, 0)
    canvas.add(zebra4)

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

def car1():
    car = Layer()

    tire1 = Circle(10, Point(-20, 15))
    tire1.setBorderWidth(3)
    tire1.setBorderColor("black")
    tire1.setDepth(20)

    ribon1 = Path(Point(-20, 15), Point(-20, 25))
    ribon1.setBorderWidth(3)
    ribon1.setDepth(20)

    ribon11 = Path(Point(-20, 15), Point(-20, 5))
    ribon11.setBorderWidth(3)
    ribon11.setDepth(20)

    ribon2 = Path(Point(-20, 15), Point(-30, 15))
    ribon2.setBorderWidth(3)
    ribon2.setDepth(20)

    ribon22 = Path(Point(-20, 15), Point(-10, 15))
    ribon22.setBorderWidth(3)
    ribon22.setDepth(20)

    tire2 = Circle(10, Point(20, 15))
    tire2.setBorderWidth(3)
    tire2.setBorderColor("black")
    tire2.setDepth(20)

    ribon3 = Path(Point(20, 15), Point(20, 5))
    ribon3.setBorderWidth(3)
    ribon3.setDepth(20)

    ribon33 = Path(Point(20, 15), Point(20, 25))
    ribon33.setBorderWidth(3)
    ribon33.setDepth(20)

    ribon4 = Path(Point(20, 15), Point(10, 15))
    ribon4.setBorderWidth(3)
    ribon4.setDepth(20)

    ribon44 = Path(Point(20, 15), Point(30, 15))
    ribon44.setBorderWidth(3)
    ribon44.setDepth(20)

    body = Rectangle(70, 30, Point(0,0))
    body.setFillColor("Blue")

    window = Polygon(Point(-5, -12), Point(33, -12), Point(13, -42), Point(-5, -42))
    window.setBorderColor("black")
    window.setBorderWidth(4)
    body.setDepth(45)

    car.add(tire1)
    car.add(ribon1)
    car.add(ribon11)
    car.add(ribon2)
    car.add(ribon22)

    car.add(tire2)

    car.add(ribon3)
    car.add(ribon33)

    car.add(ribon4)
    car.add(ribon44)

    car.add(body)
    car.add(window)

    canvas.add(car)

    car.moveTo(250, 125)
    car.setDepth(10)
    car.scale(0.75)

    def car_animation():
        x = 250
        for i in range(155):
            car.moveTo(x, 100)
            x += 5
            time.sleep(0.025)

            tire1.rotate(25)
            tire2.rotate(25)

            ribon1.rotate(25)
            ribon11.rotate(25)

            ribon2.rotate(25)
            ribon22.rotate(25)

            ribon3.rotate(25)
            ribon33.rotate(25)

            ribon4.rotate(25)
            ribon44.rotate(25)

            time.sleep(0.0005)
    
    threading.Thread(target=car_animation).start()

def car2():
    car = Layer()
    body = Polygon(Point(773, 295), Point(955, 295), Point(955, 255),  Point(773, 255))
    body.setFillColor("blue")
    car.add(body)

    window = Polygon(Point(953, 257), Point(935, 230), Point(785, 230), Point(775, 257))
    window.setBorderWidth(5)
    window.setBorderColor("white")
    car.add(window)
    tire = Layer()

    tire1 = Circle(10)
    tire1.moveTo(-20, 15)
    tire1.setBorderWidth(3)
    tire1.setDepth(45)

    tire2_layer = Layer()

    tire2 = Circle(20)
    tire2.moveTo(20, 30)
    tire2.setBorderWidth(3)
    tire2.setDepth(45)


    ribon1 = Path(Point(-20, 15), Point(-20, 25))
    ribon1.setBorderWidth(3)
    ribon1.setDepth(20)

    ribon11 = Path(Point(-20, 15), Point(-20, 5))
    ribon11.setBorderWidth(3)
    ribon11.setDepth(20)

    ribon2 = Path(Point(-20, 15), Point(-30, 15))
    ribon2.setBorderWidth(3)
    ribon2.setDepth(20)

    ribon22 = Path(Point(-20, 15), Point(-10, 15))
    ribon22.setBorderWidth(3)
    ribon22.setDepth(20)

    tire2 = Circle(10, Point(20, 15))
    tire2.setBorderWidth(3)
    tire2.setBorderColor("black")
    tire2.setDepth(20)

    ribon3 = Path(Point(20, 15), Point(20, 5))
    ribon3.setBorderWidth(3)
    ribon3.setDepth(20)

    ribon33 = Path(Point(20, 15), Point(20, 25))
    ribon33.setBorderWidth(3)
    ribon33.setDepth(20)

    ribon4 = Path(Point(20, 15), Point(10, 15))
    ribon4.setBorderWidth(3)
    ribon4.setDepth(20)

    ribon44 = Path(Point(20, 15), Point(30, 15))
    ribon44.setBorderWidth(3)
    ribon44.setDepth(20)

    tire.add(tire1)
    tire.add(ribon1)
    tire.add(ribon11)

    tire.add(ribon2)
    tire.add(ribon22)
    tire2_layer.add(tire2)
    tire2_layer.add(ribon3)
    tire2_layer.add(ribon33)

    tire2_layer.add(ribon4)
    tire2_layer.add(ribon44)

    tire2_layer.moveTo(35, 0)
    tire.add(tire2_layer)
    tire.setDepth(10)
    
    canvas.add(car)
    canvas.add(tire)
    tire.moveTo(230, 465)
    
    car.scale(0.75)
    car.moveTo(-400, 260)
    car.setDepth(20)

    def car_animation():
        x = -400
        y = 230
        for i in range(100):
            car.moveTo(x, 260)
            tire.moveTo(y, 465)
            x += 10
            y += 10
            time.sleep(0.05)
            tire1.rotate(25)
            tire2.rotate(25)

            ribon1.rotate(25)
            ribon11.rotate(25)

            ribon2.rotate(25)
            ribon22.rotate(25)

            ribon3.rotate(25)
            ribon33.rotate(25)

            ribon4.rotate(25)
            ribon44.rotate(25)

            time.sleep(0.0005)

    thread = threading.Thread(target=car_animation)
    thread.start()
    thread.join()

def cloud():
    cloud = Layer()

    circle1 = Circle(15)
    circle2 = Circle(30)
    circle3 = Circle(20)
    circle4 = Circle(10)

    circle1.setFillColor("white")
    circle1.setBorderColor("transparent")
    circle2.setFillColor("white")
    circle2.setBorderColor("transparent")
    circle3.setFillColor("white")
    circle3.setBorderColor("transparent")
    circle4.setFillColor("white")
    circle4.setBorderColor("transparent")

    circle1.moveTo(0, 25)
    circle2.moveTo(25, 10)
    circle3.moveTo(50, 12)
    circle4.moveTo(67, 20)

    cloud.add(circle1)
    cloud.add(circle2)
    cloud.add(circle3)
    cloud.add(circle4)
   
    cloud.move(40, 40)
    cloud.setDepth(35)

    canvas.add(cloud)

    cloud2 = cloud.clone()
    cloud2.moveTo(130, 40)
    canvas.add(cloud2)

def light1():
    light = Layer()

    pole = Path(Point(120, 400), Point(120, 300), Point(150, 300))
    pole.setBorderColor("blue")
    pole.setBorderWidth(5)
    bulb = Circle(5)
    bulb.setFillColor("yellow")
    bulb.setBorderColor("transparent")
    bulb.moveTo(150, 300) 
    

    light.add(pole)
    light.add(bulb)
    canvas.add(light)

    light2 = light.clone()
    light2.moveTo(15, -55)
    canvas.add(light2)

    light3 = light.clone()
    light3.moveTo(30, -105)
    canvas.add(light3)
    
    light4 = light.clone()
    light4.moveTo(45, -155)
    canvas.add(light4)
    light4.setDepth(55)
    
    light5 = light.clone()
    light5.moveTo(60, -205)
    canvas.add(light5)
    light5.setDepth(55)

def light2():
    light = Layer()

    pole = Path(Point(1210, 350), Point(1210, 250), Point(1170, 250))
    pole.setBorderColor("blue")
    pole.setBorderWidth(5)
    bulb = Circle(5)
    bulb.setFillColor("yellow")
    bulb.setBorderColor("transparent")
    bulb.moveTo(1170, 250) 

    light.add(pole)
    light.add(bulb)

    canvas.add(light)

    light2 = light.clone()
    light2.moveTo(-20, -55)
    canvas.add(light2)

    light3 = light.clone()
    light3.moveTo(-35, -105)
    canvas.add(light3)

    light4 = light.clone()
    light4.moveTo(-55, -155)
    canvas.add(light4)
    light4.setDepth(55)

def wind_turbine():
    pole1 = Path(Point(100, 300), Point(100, 200))
    pole1.setBorderColor("white")
    pole1.setBorderWidth(8)
    canvas.add(pole1)

    blade11 = Path(Point(100,200),Point(100,250))
    blade11.setBorderColor("white")
    blade11.setBorderWidth(5)
    canvas.add(blade11)

    blade12 = Path(Point(100,200),Point(143,175))
    blade12.setBorderColor("white")
    blade12.setBorderWidth(5)
    canvas.add(blade12)

    blade13 = Path(Point(100,200),Point(57,175))
    blade13.setBorderColor("white")
    blade13.setBorderWidth(5)
    canvas.add(blade13)

    pole2 = Path(Point(40, 300), Point(40, 200))
    pole2.setBorderColor("white")
    pole2.setBorderWidth(8)
    canvas.add(pole2)

    blade21 = Path(Point(40,200),Point(40,250))
    blade21.setBorderColor("white")
    blade21.setBorderWidth(5)
    canvas.add(blade21)

    blade22 = Path(Point(40,200),Point(-3,175))
    blade22.setBorderColor("white")
    blade22.setBorderWidth(5)
    canvas.add(blade22)

    blade23 = Path(Point(40,200),Point(83,175))
    blade23.setBorderColor("white")
    blade23.setBorderWidth(5)
    canvas.add(blade23)

    def blade_animation():
        while True:
            blade11.rotate(25)
            blade12.rotate(25)
            blade13.rotate(25)
            blade21.rotate(25)
            blade22.rotate(25)
            blade23.rotate(25)
            time.sleep(0.05)

    threading.Thread(target=blade_animation).start()

def tree():
    tree1 = Layer()
    
    triangle1 = Polygon(Point(325, 200), Point(375, 200), Point(350, 150))
    triangle1.setFillColor("green")
    triangle1.setBorderColor("transparent")
    tree1.add(triangle1)

    triangle2 = Polygon(Point(325, 175), Point(375, 175), Point(350, 125))
    triangle2.setFillColor("green")
    triangle2.setBorderColor("transparent")
    tree1.add(triangle2)

    stem = Path(Point(350, 200), Point(350, 225))
    stem.setBorderWidth(7)
    stem.setBorderColor("brown")
    tree1.add(stem)

    tree1.scale(0.65)
    tree1.moveTo(75, 10)
    canvas.add(tree1)
    tree1.setDepth(5)

    tree2 = tree1.clone()
    tree2.moveTo(350, 10)
    canvas.add(tree2)

    tree3 = tree1.clone()
    tree3.moveTo(675, 10)
    canvas.add(tree3)

    tree4 = Layer()

    circle1 = Circle(20)
    circle1.moveTo(400, 140)
    circle1.setFillColor("green")
    circle1.setBorderColor("transparent")
    tree4.add(circle1)

    circle2 = Circle(20)
    circle2.moveTo(380, 160)
    circle2.setFillColor("green")
    circle2.setBorderColor("transparent")
    tree4.add(circle2)

    circle3 = Circle(20)
    circle3.moveTo(420, 160)
    circle3.setFillColor("green")
    circle3.setBorderColor("transparent")
    tree4.add(circle3)

    stem2 = Path(Point(400, 200), Point(400, 168))
    stem2.setBorderWidth(7)
    stem2.setBorderColor("brown")
    tree4.add(stem2)

    
    tree4.scale(0.65)
    tree4.moveTo(175, 25)
    canvas.add(tree4)
    tree4.setDepth(5)

    tree5 = tree4.clone()
    tree5.moveTo(480, 25)
    canvas.add(tree5)

    tree6 = tree4.clone()
    tree6.moveTo(780, 25)
    canvas.add(tree6)
    
    layer = Layer()
    tree7 = tree1.clone()
    tree7.moveTo(350, 100)
    layer.add(tree7)

    tree8 = tree1.clone()
    tree8.moveTo(560, 250)
    layer.add(tree8)

    tree9 = tree4.clone()
    tree9.moveTo(450, 150)
    layer.add(tree9)

    tree10 = tree1.clone()
    tree10.moveTo(450, 180)
    layer.add(tree10)

    tree11 = tree4.clone()
    tree11.moveTo(590, 250)
    layer.add(tree11)

    canvas.add(layer)

    layer2 = layer.clone()
    layer2.moveTo(-150, -20)
    canvas.add(layer2)

    tree12 =tree1.clone()
    tree12.moveTo(550, 180)
    canvas.add(tree12)

    tree13 =tree4.clone()
    tree13.moveTo(330, 160)
    canvas.add(tree13)

    tree14 =tree4.clone()
    tree14.moveTo(600, 110)
    canvas.add(tree14)
    
def football_field():
    field = Layer()
    rectangle1 = Polygon(Point(915, 300), Point(973, 300), Point(963, 405), Point(905, 405))
    rectangle1.setBorderWidth(3)
    rectangle1.setFillColor("green")
    rectangle1.setBorderColor("white")
    field.add(rectangle1)

    circle = Circle(9)
    circle.moveTo(940, 353)
    circle.setBorderWidth(3)
    circle.setBorderColor("white")
    field.add(circle)

    line = Path(Point(966, 353), Point(910, 353))
    line.setBorderColor("white")
    line.setBorderWidth(3)
    field.add(line)

    goal_line1 = Polygon(Point(916, 405), Point(916, 389), Point(956, 389), Point(956, 405))
    goal_line1.setBorderColor("white")
    goal_line1.setBorderWidth(3)
    field.add(goal_line1)
 
    goal_line2 = Polygon(Point(920, 300), Point(920, 316), Point(960, 316), Point(960, 300))
    goal_line2.setBorderColor("white")
    goal_line2.setBorderWidth(3)
    field.add(goal_line2)
 
    canvas.add(field)
    field.moveTo(10, 5)
    field.scale(1.45)
    field.moveTo(-420, -220)

def landing_pad():
    pad = Layer()

    square = Polygon(Point(480, 150),  Point(720, 155), Point(775, 345), Point(525, 350))
    square.setFillColor((87, 87, 86))
    pad.add(square)

    circle = Circle(70)
    circle.moveTo(630, 250)
    circle.setBorderColor("yellow")
    circle.setBorderWidth(7)
    pad.add(circle)

    h = Polygon(Point(600, 300), Point(620, 300), Point(620, 255), Point(640, 255), Point(640,  300), Point(660, 300), Point(660, 200), Point(640, 200), Point(640, 235), Point(620, 235), Point(620, 200), Point(600, 200))
    h.setBorderColor("white")
    h.setBorderWidth(5)
    pad.add(h)

    line = Polygon(Point(485, 155), Point(720, 155), Point(775, 345), Point(530, 345))
    line.setBorderColor("white")
    line.setBorderWidth(3)
    pad.add(line)

    pad.scale(0.55)
    pad.moveTo(100, 150)
    canvas.add(pad)

def plane():
    plane = Layer()

    polygon1 = Polygon(Point(200, 200), Point(220, 200), Point(300, 250), Point(725, 250), Point(765, 300), Point(340, 300), Point(200, 270), Point(230, 255))
    plane.add(polygon1)
    polygon1.setFillColor("white")
    polygon1.setBorderWidth(5)

    polygon2 = Polygon(Point(450, 250), Point(450, 200), Point(470, 200), Point(500, 250))
    plane.add(polygon2)
    polygon2.setFillColor("white")
    polygon2.setBorderWidth(5)

    polygon3 = Polygon(Point(450, 300), Point(500, 300), Point(495, 320), Point(385, 395), Point(365,400))
    polygon3.setFillColor("white")
    plane.add(polygon3)
    polygon3.setBorderWidth(5)

    polygon4 = Polygon(Point(300, 270), Point(250, 270), Point(220, 300))
    polygon4.setFillColor("white")
    plane.add(polygon4)
    polygon4.setBorderWidth(5)

    polygon5 = Polygon(Point(270, 205),  Point(295, 230), Point(300, 240), Point(275, 230))
    polygon5.setFillColor("white")
    plane.add(polygon5)
    polygon5.setBorderWidth(5)

    door1 = Rectangle(10, 20, Point(350, 275))
    plane.add(door1)
    door1.setBorderWidth(3)

    door2 = Rectangle(10, 20, Point(500, 275))
    plane.add(door2)
    door2.setBorderWidth(3)

    door3 = Rectangle(10, 20, Point(650, 275))
    plane.add(door3)
    door3.setBorderWidth(3)

    window = Layer()

    window1 = Rectangle(5, 7, Point(420, 277))
    window1.setFillColor("black")
    window.add(window1)

    window2 = Rectangle(5, 7, Point(430, 277))
    window2.setFillColor("black")
    window.add(window2)

    window3 = Rectangle(5, 7, Point(440, 277))
    window3.setFillColor("black")
    window.add(window3)

    window4 = Rectangle(5, 7, Point(450, 277))
    window4.setFillColor("black")
    window.add(window4)

    window5 = Rectangle(5, 7, Point(460, 277))
    window5.setFillColor("black")
    window.add(window5)

    window6 = Rectangle(5, 7, Point(470, 277))
    window6.setFillColor("black")
    window.add(window6)

    window7 = Rectangle(5, 7, Point(480, 277))
    window7.setFillColor("black")
    window.add(window7)

    window8 = Rectangle(5, 7, Point(490, 277))
    window8.setFillColor("black")
    window.add(window8)

    window.moveTo(-25, 0)
    plane.add(window)

    layer2 = window.clone()
    layer2.moveTo(125, 0)
    plane.add(layer2)

    roop = Path(Point(225, 250), Point(100, 250))
    roop.setBorderColor("black")
    roop.setBorderWidth(5)
    plane.add(roop)

    flag = Rectangle(200, 100, Point(50, 250))
    flag.setFillColor("white")
    plane.add(flag)
    flag.setBorderColor("black")
    flag.setBorderWidth(3)
    
    plane.moveTo(100, 0)

    text = Layer()

    color = (255, 0, 0)
    text1 = Text("Programmed", 20)
    text1.moveTo(100, 100)
    text.add(text1)
    text1.setFontColor(color)

    text2 = Text("By", 20)
    text2.moveTo(110, 130)
    text2.setFontColor(color)
    text.add(text2)

    text3 = Text("Ammar Sabit", 20)
    text3.moveTo(100, 160)
    text3.setFontColor(color)
    text.add(text3)
    text.moveTo(-50, 115)

    plane.add(text)

    canvas.add(plane)
    plane.setDepth(5)
    plane.scale(0.5)

    plane.moveTo(-400, -80)

    def plane_animation():
        x = -400
        for i in range(420):
            plane.moveTo(x, -80)
            x += 4
            time.sleep(0.005)

    plane_animation()

geda_gate()
main_gate()
text()
road()
tree()
green_area()
fence()
road_lane1()
road_lane2()
road_lane3()
road_lane4()
zebra()
cloud()
light1()
light2()
football_field()
landing_pad()
# scale()
wind_turbine()
car1()
car2()
plane()