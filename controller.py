#Controller Script for ECE306
#
#Controller MUST be connected for this to work
#

from inputs import get_gamepad #INSTALL THIS PACKAGE: "pip install inputs"

import socket
#---------------------------------------------------------

ip = "192.168.70.24" #IP GOES HERE
port = 8080 #PORT GOES HERE

#---------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the server
s.connect((ip, port))

wheel_time = 5 #i used this to make my car go for a certain amount of time

print("the socket has successfully connected to the car")

while 1:
  events = get_gamepad()
  for event in events:

    print(event.code, event.state)
    #s.send(bytes("^[PIN][COMMAND][TIMER]\r\n", "utf-8"))

    if event.code == "BTN_TR" and event.state == 1:    #python3.10 has switch statements to clean this up BTN_TR
      print("Right Bumper pressed")
      #if ((wheel_time + 1) < 50): #example command for changing wheel time
      #  wheel_time += 1
      s.send(bytes("^8534R1\r\n", "utf-8"))

    elif  event.code == "BTN_TL" and event.state == 1:
      print("Left Bumper pressed")
      #if ((wheel_time - 1) > 0): #example command for changing wheel time
      #  wheel_time -= 1
      s.send(bytes("^8534L1\r\n", "utf-8"))


#
    elif  event.code == "BTN_WEST" and event.state == 1:
      print("X pressed")
      #if ((wheel_time - 1) > 0): #example command for changing wheel time
      #  wheel_time -= 1
      s.send(bytes("^8534X4\r\n", "utf-8"))

    elif  event.code == "BTN_NORTH" and event.state == 1:
      print("Y pressed")
      #if ((wheel_time - 1) > 0): #example command for changing wheel time
      #  wheel_time -= 1
      s.send(bytes("^8534SH\r\n", "utf-8"))

    elif event.code == "BTN_SOUTH" and event.state == 1:
      print("A pressed")
      s.send(bytes("^8534F3\r\n", "utf-8")) #exmaple command for going forward

    elif event.code == "BTN_EAST" and event.state == 1:
      print("B pressed")
      s.send(bytes("^8534B2\r\n", "utf-8")) #exmaple command for going forward

    elif event.code == "ABS_RZ" and event.state == 1:
      print("R2 pressed")
      s.send(bytes("^8534R2\r\n", "utf-8")) #exmaple command for going forward

    elif event.code == "ABS_RY" and event.state == 1:
      print("L2 pressed")
      s.send(bytes("^8534L2\r\n", "utf-8")) #exmaple command for going forward


    elif event.code == "ABS_HAT0Y" and event.state == -1:
      print("Upper D pressed")
      s.send(bytes("^8534F1\r\n", "utf-8"))  # exmaple command for going forward

    elif event.code == "ABS_HAT0Y" and event.state == 1:
      print("Lower D pressed")
      s.send(bytes("^8534B1\r\n", "utf-8"))  # exmaple command for going forward

    elif event.code == "ABS_HAT0X" and event.state == 1:
      print("Right D pressed")
      s.send(bytes("^8534R1\r\n", "utf-8"))  # exmaple command for going forward

    elif event.code == "ABS_HAT0X" and event.state == -1:
      print("Left D pressed")
      s.send(bytes("^8534L1\r\n", "utf-8"))  # exmaple command for going forward

    elif event.code == "BTN_SELECT" and event.state == 1:
      print("Right Select pressed")
      s.send(bytes("^8534DA\r\n", "utf-8"))  # exmaple command for going forward

    elif event.code == "BTN_START" and event.state == 1:
      print("Left Select pressed")
      s.send(bytes("^8534ES\r\n", "utf-8"))  # exmaple command for going forward





