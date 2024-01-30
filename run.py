import sys

sys.path.append('slova')
sys.path.append('skils')

import pyaudio
import json
import time
import random
import serial as sp
from setings import setings
from priveti import privet
from arduino_trigers import LEDon
from arduino_trigers import LEDof
from arduino import LED_of
from arduino import LED_on
from kak_dela import kak_dela
from kak_dela import otveti
from vosk import Model, KaldiRecognizer


model = Model("model")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
streem = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
streem.start_stream()


def listen():
    while True:
        data = streem.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text'].lower()

print("Дженн запущен")

for text in listen():
    
    try:
        for i in LED_on:
            if text == i:
                LEDon()

        for i in LED_of:
            if text == i:
                LEDof()
    except:
        print("Подключи ардуино к COM порту и укажи его в настройках")

    for i in privet:
        if text == i:
            print(random.choice(privet), "", setings["name"])
        
    for i in kak_dela:
        if text == i:
            print(random.choice(otveti))