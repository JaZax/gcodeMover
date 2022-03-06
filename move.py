from msilib.schema import ListBox
import serial
import time
import tkinter as tk
from tkinter import ttk



import serial.tools.list_ports
getPorts = serial.tools.list_ports.comports()
ports = []
for port in sorted(getPorts):
  ports.append(str(port))

def mapper(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def connect():
  comChoose = comPortChoose.get()
  if comChoose:
    global comPort
    comPort = ""

    for i in range(len(comChoose)):
      if(comChoose[i] != " "):
        comPort += comChoose[i]
      
      if(comChoose[i] == " "):
        break

    global ser
    ser = serial.Serial(comPort, 115200)

def sendCommand(ser, command):
  ser.write(str.encode(command)) 
  time.sleep(1)

  while True:
    line = ser.readline()
    print(line)

    if line == b'ok\n':
      break
  
time.sleep(2)

root = tk.Tk()

root.title("gcodeMover")
root.geometry("400x400")
root.resizable(False, False)

topFrame = tk.Frame(root)
topFrame.pack()

n = tk.StringVar()
comPortChoose = ttk.Combobox(topFrame, width = 25, textvariable=n, value=ports)
comPortChoose.grid(column=1, row=1)

connectButton = tk.Button(topFrame, text="Connect", command = lambda: connect())
connectButton.grid(column=2, row=1)

homingButton = tk.Button(root, text="Home all axes", command = lambda: sendCommand(ser,"G28 \r\n"))
homingButton.pack()

#root.bind("<Button-1>", click)

root.mainloop()




#def click(event):
#  print("clicked at", event.x, event.y)
#
#  yPos = mapper(event.y, 0, int(bedY), int(bedY), 0)
#
#  sendCommand(ser, "G0 F3500" + " X" + str(event.x) + " Y" + str(yPos) + " \r\n")