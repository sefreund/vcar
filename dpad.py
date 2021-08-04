from time import sleep
from gpiozero import Robot
from bluedot import BlueDot
from signal import pause
from picamera import PiCamera

#Lib for EMail
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

robby = Robot(left=(9,10),right=(7,8))

tleft=0.85
tright=0.85
cam = PiCamera()

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
    bd = BlueDot(cols=3, rows=3)
    bd.square = True
    bd[0,0].square = False
    bd[2,0].square = False
    bd[0,2].square = False
    bd[2,2].square = False
    bd[1,1].square = False 
    bd[1,0].color = "gray40"
    bd[1,2].color = "gray40"
    bd[0,1].color = "gray40"
    bd[2,1].color = "gray40"
    bd[1,0].when_pressed = up
    bd[1,2].when_pressed = down
    bd[0,1].when_pressed = left
    bd[2,1].when_pressed = right
    bd[1,1].when_pressed = take_picture
    bd[1,1].color = "red4"
    bd[0,0].color = "deepskyblue"
    bd[2,0].color = "coral"
    bd[0,2].color = "mediumseagreen"
    bd[2,2].color = "goldenrod2"
    


    #O.M  1.sky blue, 4.yellow green, 3.light goldenrod, 2.coral, 
    #V.D 1.deep sky blue, 3.lawn green, 2.medium sea green,4.DarkOrange2
 
def send_email():
    subject = "Neues Foto vcar "
    body = "Hallo, ich bin vcar. Im Anhang findest du ein Foto von dir/was was die gehötr/..."
    sender_email = "vcar.python@gmail.com"
    receiver_email = "antboyxxx@gmail.com"
    password = "fluchderkaribikpiano"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "pic.jpg"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()


    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    print('Martin&Vincent checken  einfach alles')
    
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def take_picture():
    cam.capture("pic.jpg")
    send_email()
    print('E Mail versendet an vincent')

def up(pos):    
    if pos.x>0.3:
        robby.forward(1, curve_right=(pos.x))
    elif pos.x<-0.3:
        robby.forward(1, curve_left=abs(pos.x))
    print('Martin ist der coolste')   
   
  

def right():
    robby.right(1)

def left():
    robby.left(1)
    
def down(pos):
        if pos.x > 0.3:
            robby.backward(1, curve_right=pos.x)
        elif pos.x<-0.3:
            robby.backward(1, curve_left=abs(pos.x))

        


def stop(pos):
    robby.stop()



if __name__ == '__main__':
    remoteAndroid()
    while True: pass

