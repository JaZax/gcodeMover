import serial
import time
import tkinter as tk

bedX = input("x bed dimension: \n")
bedY = input("y bed dimension: \n")
port = input("COM port: \n")

ser = serial.Serial(port, 115200)

def command(ser, command):
  #start_time = datetime.now()
  ser.write(str.encode(command)) 
  time.sleep(1)

  while True:
    line = ser.readline()
    print(line)

    if line == b'ok\n':
      break

def click(event):
    print("clicked at", event.x, event.y)

    command(ser, "G0 F3500" + " X" + str(event.x) + " Y" + str(event.y) + " \r\n")

time.sleep(2)
command(ser, "G28\r\n")

root = tk.Tk()

root.title("gcodeMover")
root.geometry(bedX + "x" + bedY)

root.bind("<Button-1>", click)

root.mainloop()

