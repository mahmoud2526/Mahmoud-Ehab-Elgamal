from tkinter import *


import serial


def start_pump():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600


    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")
        command = "start"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def stop_pump():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

      # Wait for the connection to be established

        command = "stop"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def right():

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

          # Wait for the connection to be established

        command = "right"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def left():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

          # Wait for the connection to be established

        command = "left"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def down():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

          # Wait for the connection to be established

        command = "down"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def front():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

         # Wait for the connection to be established

        command = "front"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def Mright():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

         # Wait for the connection to be established

        command = "mright"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def mleft():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

         # Wait for the connection to be established

        command = "mleft"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def back():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

         # Wait for the connection to be established

        command = "back"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def up():
    bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
    baud_rate = 9600

    try:
        bluetooth = serial.Serial(bluetooth_port, baud_rate)
        print(f"Connected to Bluetooth module on {bluetooth_port}")

        # Wait for the connection to be established

        command = "up"
        bluetooth.write(command.encode())  # Send the command
        print(f"Sent: {command}")

        bluetooth.close()  # Close the connection

    except serial.SerialException as e:
        print(f"Could not open port {bluetooth_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")




FONT_NAME = "Courier"

# Initialize the main window
window = Tk()
window.title("Firefighting Robot")
window.minsize(600, 600)
window.maxsize(600, 600)

# Create a Canvas widget
canva = Canvas(window, width=600, height=600, highlightthickness=0)
canva.place(x=0, y=0)

# Load another image for the canvas
photo = PhotoImage(file="Untitled design.png")
image_phot = canva.create_image(300, 300, image=photo)
sphoto = PhotoImage(file="play-solid.png")
# Create a Button widget with the resized image
#start

start=Button(window,text="▶",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=start_pump)
start.place(x=290, y=50)

# Keep a reference to the image object to prevent garbage collection
#stop

stop=Button(window,text="❚❚",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=stop_pump)
stop.place(x=290, y=100)

#pump up

up=Button(window,text="▲",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=up)
up.place(x=290, y=150)

#pump right

right=Button(window,text="▶",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=right)
right.place(x=400, y=200)


#pump left

left=Button(window,text="◀",border=0.5,fg="black",width=6,bg=None
             ,font=(FONT_NAME,14),command=left)
left.place(x=180, y=200)

#pump down

down=Button(window,text="▼",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=down)
down.place(x=290, y=250)



#front

front=Button(window,text="▲",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=front)
front.place(x=290, y=350)

#m right

Mright=Button(window,text="▶",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=Mright)
Mright.place(x=400, y=400)


#m left

Mleft=Button(window,text="◀",border=0.5,fg="black",width=6,bg=None
             ,font=(FONT_NAME,14),command=mleft)
Mleft.place(x=180, y=400)

#back

back=Button(window,text="▼",border=0.5,fg="black",width=6
             ,font=(FONT_NAME,14),command=back)
back.place(x=290, y=450)
#function
















































# Run the Tkinter event loop
window.mainloop()

