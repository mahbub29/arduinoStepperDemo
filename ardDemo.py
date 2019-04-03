import serial
import tkinter

arduinoData = serial.Serial('com7',9600)

############################################

def led1_on():
     arduinoData.write('1'.encode())
     print("LED-1 ON")
def led1_off():
     arduinoData.write('0'.encode())
     print("LED-1 OFF")

def led2_on():
    arduinoData.write('2'.encode())
    print("LED-2 ON")
def led2_off():
    arduinoData.write('3'.encode())
    print("LED-2 OFF")


def led3_on():
    arduinoData.write('4'.encode())
    print("LED-3 ON")
def led3_off():
    arduinoData.write('5'.encode())
    print("LED-3 OFF")

def led4_on():
    arduinoData.write('6'.encode())
    print("LED-4 ON")
def led4_off():
    arduinoData.write('7'.encode())
    print("LED-4 OFF")

def led5_on():
    arduinoData.write('8'.encode())
    print("LED-5 ON")
def led5_off():
    arduinoData.write('9'.encode())
    print("LED-5 OFF")

def all_on():
    arduinoData.write('t'.encode())
    print("ALL LEDs ON")
def all_off():
    arduinoData.write('n'.encode())
    print("ALL LEDs OFF")

def lightshow():
    arduinoData.write('a'.encode())
    print("Taaa-daaaaaa!")

#########################################

led_control_window = tkinter.Tk()

Button = tkinter.Button

btn = Button(led_control_window, text = "LED1-ON", command = led1_on)
btn1 = Button(led_control_window, text = "LED1-OFF", command = led1_off)
btn2 = Button(led_control_window, text = "LED2-ON", command = led2_on)
btn3 = Button(led_control_window, text = "LED2-OFF", command = led2_off)
btn4 = Button(led_control_window, text = "LED3-ON", command = led3_on)
btn5 = Button(led_control_window, text = "LED3-OFF", command = led3_off)
btn6 = Button(led_control_window, text = "LED4-ON", command = led4_on)
btn7 = Button(led_control_window, text = "LED4-OFF", command = led4_off)
btn8 = Button(led_control_window, text = "LED5-ON", command = led5_on)
btn9 = Button(led_control_window, text = "LED5-OFF", command = led5_off)
btn10 = Button(led_control_window, text = "ALL-ON", command = all_on)
btn11 = Button(led_control_window, text = "ALL-OFF", command = all_off)
btn12 = Button(led_control_window, text = "LightShow", command = lightshow)

btn.grid(row = 0, column = 0, sticky = 'EW')
btn1.grid(row = 0, column = 1, sticky = 'EW')
btn2.grid(row = 1, column = 0, sticky = 'EW')
btn3.grid(row = 1, column = 1, sticky = 'EW')
btn4.grid(row = 2, column = 0, sticky = 'EW')
btn5.grid(row = 2, column = 1, sticky = 'EW')
btn6.grid(row = 3, column = 0, sticky = 'EW')
btn7.grid(row = 3, column = 1, sticky = 'EW')
btn8.grid(row = 4, column = 0, sticky = 'EW')
btn9.grid(row = 4, column = 1, sticky = 'EW')
btn10.grid(row = 5, column = 0, sticky = 'EW')
btn11.grid(row = 5, column = 1, sticky = 'EW')
btn12.grid(row = 6, column = 0, columnspan = 2, sticky = 'EW')

led_control_window.mainloop()

input("Press Enter to exit")