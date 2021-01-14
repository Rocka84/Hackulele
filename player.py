from __future__ import print_function
import time

from song import Song

class Player():
  """Animator for a Song."""

  def __init__(self, populele, song = None):
    self._populele = populele
    self.interval = 1
    self.song = None
    if song is not None:
        self.setSong(song)

  def setPopulele(self, populele):
      self._populele = populele

  def _SetFret(self, string, fret):
    self._populele.SetFret(string, fret, self._populele.LED_ON)

  def _setChord(self, chord):
    self._populele.SetAll(self._populele.LED_OFF)
    frets = chord.getFrets()
    for string in range(4):
        if frets[string][0] > 0:
            self._SetFret(string + 1, frets[string][0])

  def nextChord(self):
      self.song.nextElement()
      self.draw()

  def prevChord(self):
      self.song.prevElement()
      self.draw()

  def setSong(self, song):
    self.song = song
    self.interval = 60.0 / self.song.getBPM()
    print("new interval")
    print(self.interval)
    self.reset()

  def reset(self):
      self.song.reset()
      self.draw()

  def beat(self):
      self.song.beat()
      self.draw()

  def getCurrentChord(self):
      return self.song.getCurrentChord()

  def getCurrentChordName(self):
      return self.song.getCurrentChord().getName()

  def draw(self):
    self._setChord(self.song.getCurrentChord())
    self._populele.ShowFrame()

