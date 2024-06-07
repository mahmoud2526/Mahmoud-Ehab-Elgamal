import serial
import time

# Replace 'COM3' with the port your Bluetooth module is connected to
bluetooth_port = 'COM9'  # Example for Windows
# For Mac/Linux, it might be something like '/dev/tty.HC-05-DevB'
baud_rate = 9600

try:
    bluetooth = serial.Serial(bluetooth_port, baud_rate)
    print(f"Connected to Bluetooth module on {bluetooth_port}")

    time.sleep(2)  # Wait for the connection to be established

    command = "start"
    bluetooth.write(command.encode())  # Send the command
    print(f"Sent: {command}")

    bluetooth.close()  # Close the connection

except serial.SerialException as e:
    print(f"Could not open port {bluetooth_port}: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
