import machine
import time
import json

led = machine.Pin("LED", machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(1, machine.Pin.OUT))
buzzer.freq(10000)
buzzer.duty_u16(12768) # controlls volume

led.on()

note_separator = 0.005 # seconds
slow_down_rate = 1

buzzer_list = []

with open('buzzer_notes.json', 'r') as file:
    buzzer_list = json.load(file)

while True:
    for note in buzzer_list:
        print(note)
        if note["frequency"] == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.duty_u16(12768)
            buzzer.freq( int(note["frequency"]))

        duration = float(note["duration"])
        if duration > 5:
            duration = 5
        time.sleep( duration * slow_down_rate - note_separator )
        buzzer.duty_u16(0)
        time.sleep(note_separator)
