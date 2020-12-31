from __future__ import print_function
import time
import sys
import signal
import buttonshim

from bluezpopulele import BlueZPopulele
from player import Player

from song.examples.testsong import TestSong
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
        self.stroke = 0
        self.populele = None
        self.player = None
        self.song = None
        self.song_id = 0

    def showBeat(self, value = None):
        if value is not None:
            self.stroke = value
        else:
            self.stroke = self.stroke + 1
            if self.stroke > 4:
                self.stroke = 1

        if self.stroke == 0 or self.stroke == 1:
            self.populele.SetFret(4, 14, value)
        if self.stroke == 2:
            self.populele.SetFret(3, 14, value)
        if self.stroke == 3:
            self.populele.SetFret(2, 14, value)
        if self.stroke == 4:
            self.populele.SetFret(1, 14, value)

        self.populele.ShowFrame()

        if self.stroke == 1 or self.stroke == 3:
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
        self.showPauseState()
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
            self.showBeat()
            time.sleep(self.player.interval)

    def setSong(self, song):
        self.song = song
        if self.player is not None:
            self.player.setSong(self.song)

    def nextChord(self):
        self.player.nextChord()
        self.showBeat(0)
        print("Next Chord")
        print(self.player.getCurrentChord())

    def prevChord(self):
        self.player.prevChord()
        self.showBeat(0)
        print("Prev Chord")
        print(self.player.getCurrentChord())

    def resetSong(self):
        self.setPaused(True)
        self.player.reset()
        self.showBeat(0)
        print("Reset Song")

    def showPauseState(self):
        value = 0xFF if self.paused else 0
        self.populele.SetFret(1, 9, value)
        self.populele.SetFret(2, 9, value)
        self.populele.SetFret(3, 9, value)
        self.populele.SetFret(4, 9, value)
        self.populele.SetFret(1, 11, value)
        self.populele.SetFret(2, 11, value)
        self.populele.SetFret(3, 11, value)
        self.populele.SetFret(4, 11, value)
        self.populele.ShowFrame()

    def nextSong(self):
        self.song_id += 1
        if self.song_id > 2:
            self.song_id = 0
        self.setSong(self.loadSongById(self.song_id))
        print("Load song %i" % self.song_id)


    def loadSongById(self, song_id):
        if song_id == 2:
            return RnRUebermensch()
        elif song_id == 1:
            return AllesSoEinfach()
        else:
            return TestSong()


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

@buttonshim.on_hold(buttonshim.BUTTON_B, hold_time=2)
def button_b_hold(button):
    global controller
    controller.nextSong()

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
# controller.setActive(False)

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

