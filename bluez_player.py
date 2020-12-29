from __future__ import print_function
import time
import sys
import signal
import buttonshim

from bluezpopulele import BlueZPopulele
from player import Player
from song.examples.allessoeinfach import AllesSoEinfach
from song.examples.rnruebermensch import RnRUebermensch


def handle_stop_signals(signum, frame):
    raise KeyboardInterrupt()

signal.signal(signal.SIGTERM, handle_stop_signals)

class PlayerController():
    def __init__(self):
        self.active = True
        self.playing = False
        self.paused = True
        self.led_beat = False
        self.populele = None
        self.player = None
        self.song = None

    def beatLED(self, value = None):
        if value is not None:
            self.lead_beat = value
        else:
            self.led_beat = not self.led_beat
        if self.led_beat:
            buttonshim.set_pixel(0x00, 0x33, 0x33)
        else:
            buttonshim.set_pixel(0x33, 0x00, 0x33)

    def setActive(self, value):
        self.active = value
        if not self.active:
            buttonshim.set_pixel(0x00, 0x44, 0x33)
            print("Deactivated")
        else:
            buttonshim.set_pixel(0x00, 0x00, 0x66)
            print("Activated")

    def isActive(self):
        return self.active

    def setPlaying(self, value):
        self.playing = value

    def isPlaying(self):
        return self.playing

    def setPaused(self, value):
        self.paused = value
        if self.paused:
            print("Paused")
        else:
            print("Unpaused")

    def isPaused(self):
        return self.paused

    def connect(self, populele):
        self.populele = populele
        print("Connecting")
        while self.active and not self.populele.isSetupDone():
            buttonshim.set_pixel(0x00, 0x00, 0x66)
            try:
                self.populele.Setup()
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                print("retry")
                buttonshim.set_pixel(0x00, 0x33, 0x66)
                time.sleep(1)

        if not self.active:
            return

        if self.player is None:
            self.player = Player(self.populele, self.song)
        else:
            self.player.setPopulele(populele)

        buttonshim.set_pixel(0x00, 0x66, 0x00)
        self.setPaused(True)
        self.player.draw()
        print("Ready for playback")
        print("First Chord: %s" % self.player.getCurrentChord())

    def disconnect(self):
        buttonshim.set_pixel(0x33, 0x00, 0x00)
        if self.populele is None:
            return
        if self.populele.isConnected():
            self.populele.SetAll(self.populele.LED_OFF)
            self.populele.ShowFrame()
            self.populele.Disconnect()

    def tick(self):
        if not self.populele.isConnected():
            raise Exception("Connection lost")
        elif self.paused:
            time.sleep(0.01)
        else:
            self.player.beat()
            print(self.player.getCurrentChord())
            self.beatLED()
            time.sleep(self.player.interval)

    def setSong(self, song):
        self.song = song
        if self.player is not None:
            self.player.setSong(self.song)

    def nextChord(self):
        self.player.nextChord()
        self.beatLED(True)
        print("Next Chord")
        print(self.player.getCurrentChord())

    def prevChord(self):
        self.player.prevChord()
        self.beatLED(True)
        print("Prev Chord")
        print(self.player.getCurrentChord())

    def resetSong(self):
        self.setPaused(True)
        self.player.reset()
        self.beatLED(True)
        print("Reset Song")


@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    global controller
    controller.setPaused(not controller.isPaused())

@buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
def button_a_hold(button):
    global controller
    controller.resetSong()

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    global controller
    controller.nextChord()

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    global controller
    controller.prevChord()

@buttonshim.on_hold(buttonshim.BUTTON_D, hold_time=2)
def button_d_hold(button):
    global controller
    if controller.isActive():
        controller.setActive(False)
        time.sleep(1)
    controller.setActive(True)

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    global controller
    if controller.isActive():
        return
    controller.setActive(True)

@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def button_e_hold(button):
    global controller
    controller.setActive(not controller.isActive())


controller = PlayerController()
controller.setSong(RnRUebermensch())
controller.setActive(False)

while True:
    try:
        if not controller.isActive():
            time.sleep(0.1)
            continue

        controller.connect(BlueZPopulele())
        controller.setPaused(True)

        if not controller.isActive():
            continue

        while controller.isActive():
            controller.tick()

    except KeyboardInterrupt:
        print("Exiting")
        controller.disconnect()
        buttonshim.set_pixel(0x00, 0x00, 0x00)
        sys.exit(0)

    except:
        print("Connection lost, deactivating")
        controller.setActive(False)

controller.disconnect()

