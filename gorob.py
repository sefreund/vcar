from time import sleep
from gpiozero import Robot
from bluedot import BlueDot
from signal import pause


robby = Robot(left=(9,10),right=(8,7))

tleft=0.85
tright=0.85

def line():
    robby.forward(1)
    sleep(1.15)
    robby.left(1)
    sleep(tleft)
    robby.forward(1)
    sleep(2)
    robby.right(1)
    sleep(tright)
    robby.forward(0.4)
    sleep(0.5)
    robby.left(1)
    sleep(tleft)
    robby.forward(1)                                                                          
    sleep(0.9)
    robby.stop()



def remoteAndroid():
    bd = BlueDot(
            #cols=3, rows=3
            )
 
    #bd.square = True
    #bd[0,0].visible = False
    #bd[2,0].visible = False
    #bd[0,2].visible = False
    #bd[2,2].visible = False
    #bd[1,1].visible = False

    bd.when_pressed = move ##run the function foo when the blue dot is pressed
    bd.when_released = stop ##run the function bar when the blue dot is released
    bd.when_moved = move ##run the function baz when your finger moves on the blue dot
 
def move(pos):
    print(pos)
    if pos.y > 0.2:
        if pos.x > 0:
            robby.forward(pos.y, curve_right=(pos.x))
        else:
            robby.forward(pos.y, curve_left=abs(pos.x))
    elif pos.y > -0.2:
        if pos.x > 0.2:
            robby.right(pos.x)
        else:
            robby.left(abs(pos.x))
    else:

        if pos.x > 0:
            robby.backward(abs(pos.y), curve_right=pos.x)
        else:
            robby.backward(abs(pos.y), curve_left=abs(pos.x))

        


def stop(pos):
    robby.stop()



if __name__ == '__main__':
    remoteAndroid()
    while True: 
        sleep(0.1)

