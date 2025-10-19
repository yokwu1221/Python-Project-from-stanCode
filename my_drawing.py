"""
File: my_drawing
Name: Olaf, snoopy's brother

This is Snoopy's older brother. He is always lazy and sleepy.
His nickname is the ugliest dog in the world, but I think he is the most adorable dog in the world.
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=800, height=400, title= "Olaf")

    # ear
    left_ear = GOval(50, 120, x=430, y=120)
    left_ear.filled = True
    window.add(left_ear)

    right_ear = GOval(50, 120,x= 620, y=120)
    right_ear.filled = True
    window.add(right_ear)

    # hand
    left_hand = GOval(90, 50, x=400, y=250)
    left_hand.filled= True
    left_hand.fill_color = "white"
    window.add(left_hand)
    right_hand = GOval(90, 50, x=620, y=250)
    right_hand.filled = True
    right_hand.filled= True
    right_hand.fill_color = "white"
    window.add(right_hand)

    # body
    body = GOval(220, 170, x=440, y=210)
    body.filled = True
    body.fill_color = "white"
    window.add(body)

    # face
    head = GOval(200, 120, x= 450, y= 100)
    head.filled = True
    head.fill_color = "white"
    window.add(head)

    # face_eye
    left_eye = GOval(35, 40, x= 550-10-35, y= 100+20)
    window.add(left_eye)
    left_eyeball = GArc(40, 50, 30, 180, x= 502, y=115 )
    left_eyeball.filled = True
    left_eyeball.fill_color = "beige"
    window.add(left_eyeball)
    left_point = GOval(10,10, x= 550-25, y= 100+40)
    window.add(left_point)
    left_point.filled = True

    right_eye = GOval(35, 40, x= 550+10, y= 100+20)
    window.add(right_eye)
    right_eyeball = GArc(40, 50, 360-20, 180, x= 560, y=115 )
    right_eyeball.filled = True
    right_eyeball.fill_color = "beige"
    window.add(right_eyeball)
    right_point = GOval(10,10, x= 550+30, y= 100+40)
    window.add(right_point)
    right_point.filled = True
    # face_nose
    nose= GOval(50,35, x=550-25, y= 100+50)
    window.add(nose)
    nose.filled = True

    # hat
    hat = GRect(200, 60, x= 450, y=50)
    hat.filled = True
    hat.fill_color = "royalblue"
    hat.color = "royalblue"
    window.add(hat)
    hat_front = GOval(150, 30, x=360, y=80 )
    hat_front.filled = True
    hat_front.fill_color = "royalblue"
    hat_front.color = "royalblue"
    window.add(hat_front)

    # face_mouth
    tongue = GArc(45, 112, 180, 180, x= 528, y= 172)
    tongue.filled = True
    tongue.fill_color = "red"
    window.add(tongue)
    tongue_line = GLine(550, 202, 550, 230)
    window.add(tongue_line)
    left_mouth = GArc(60, 60, 200, 160, x=490, y=170)
    window.add(left_mouth)
    right_mouth = GArc(80, 80, 160, 160, x=550, y=150)
    window.add(right_mouth)

    # leg
    lef_leg = GOval(80, 80, x=450, y=320)
    lef_leg.filled = True
    lef_leg.fill_color = "white"
    window.add(lef_leg)
    left_leg1 = GLine(460, 332, 460, 365)
    window.add(left_leg1)
    left_leg2 = GLine(485, 320, 485, 365)
    window.add(left_leg2)
    left_leg3 = GLine(510, 325, 510, 365)
    window.add(left_leg3)
    right_leg = GOval(80, 80, x=565, y=320)
    right_leg.filled = True
    right_leg.fill_color = "white"
    window.add(right_leg)
    right_leg1 = GLine(580, 332, 580, 365)
    window.add(right_leg1)
    right_leg2 = GLine(605, 320, 605, 365)
    window.add(right_leg2)
    right_leg3 = GLine(628, 326, 628, 365)
    window.add(right_leg3)

    name = GLabel("OLAF")
    name.font = "Times-90-bold"
    window.add(name, x=50, y=140)

    brother = GLabel("SNOOPY'S BROTHER")
    brother.font = "Times-30-italic"
    window.add(brother, x=50, y=200)

    dog = GLabel("No1 Ugly dog")
    dog.font = "Times-30-italic"
    window.add(dog, x=100, y=250)

if __name__ == '__main__':
    main()
