import serial as sp
from setings import setings

def LEDon():
        sp = sp.Serial(setings["arduino"], 9600)
        time.sleep(1)
        sp.write(b"on")
        print("Запрос отправлен к ардуино")

def LEDof():
        sp = sp.Serial(setings["arduino"], 9600)
        time.sleep(1)
        sp.write(b"off")
        print("Запрос отправлен к ардуино")