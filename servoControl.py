import tkinter as tk
import serial

arduinoData = serial.Serial('com7',9600)

############################################

def up():
    arduinoData.write('1'.encode())
    print("Servo at 0 deg")

def ur():
    arduinoData.write('2'.encode())
    print("Servo at 45 deg")

def right():
    arduinoData.write('3'.encode())
    print("Servo at 90 deg")

def dr():
    arduinoData.write('4'.encode())
    print("Servo at 135 deg")

def down():
    arduinoData.write('5'.encode())
    print("Servo at 180 deg")

def dl():
    arduinoData.write('6'.encode())
    print("Servo at 225 deg")

def left():
    arduinoData.write('7'.encode())
    print("Servo at 270 deg")

def ul():
    arduinoData.write('8'.encode())
    print("Servo at 315 deg")

############################################

servo_control_window = tk.Tk()

Button = tk.Button

btnUp = Button(servo_control_window, text = "UP", command = up)
btnUr = Button(servo_control_window, text = "U-R", command = ur)
btnRight = Button(servo_control_window, text = "RIGHT", command = right)
btnDr = Button(servo_control_window, text = "D-R", command = dr)
btnDown = Button(servo_control_window, text = "DOWN", command = down)
btnDl = Button(servo_control_window, text = "D-L", command = dl)
btnLeft = Button(servo_control_window, text = "LEFT", command = left)
btnUl = Button(servo_control_window, text = "U-L", command = ur)

btnUl.grid(row = 0, column = 0, sticky = 'EW')
btnUp.grid(row = 0, column = 1, sticky = 'EW')
btnUr.grid(row = 0, column = 2, sticky = 'EW')
btnLeft.grid(row = 1, column = 0, sticky = 'EW')
btnRight.grid(row = 1, column = 2, sticky = 'EW')
btnDl.grid(row = 2, column = 0, sticky = 'EW')
btnDown.grid(row = 2, column = 1, sticky = 'EW')
btnDr.grid(row = 2, column = 2, sticky = 'EW')

servo_control_window.mainloop()
