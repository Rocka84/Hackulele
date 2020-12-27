"""Swith the LEDs on over bluetooth via BlueZ"""

from __future__ import print_function

import time
import buttonshim

from pydbus import SystemBus, Variant
from bluezpopulele import BlueZPopulele

from player import Player

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    global is_playing
    is_playing = False

is_playing = True

DBUS = SystemBus()

try:
    populele = BlueZPopulele(DBUS)
    while not populele.isSetupDone():
        buttonshim.set_pixel(0x00, 0x00, 0x66)
        try:
            populele.Setup()
        except:
            print("retry")
            buttonshim.set_pixel(0x00, 0x00, 0x00)
            time.sleep(0.5)
    buttonshim.set_pixel(0x00, 0x66, 0x00)

    player = Player(populele)

    print("Starting playback")
    while is_playing:
        player.Draw()
        populele.ShowFrame()
        ival = player.interval
        while ival > 0:
            if ival > 20:
                time.sleep(0.02)
                ival -= 20
            else:
                time.sleep(ival/1000)
                ival = 0
finally:
    buttonshim.set_pixel(0x00, 0x00, 0x00)


