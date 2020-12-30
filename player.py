from __future__ import print_function
import time

from song import Song
from song.examples.allessoeinfach import AllesSoEinfach

class Player():
  """Animator for a Song."""

  def __init__(self, populele, song = None):
    self._populele = populele
    self.song = AllesSoEinfach() if song == None else song
    self.interval = 60.0 / self.song.getBPM()

  def setPopulele(self, populele):
      self._populele = populele

  def _SetFret(self, string, fret):
    self._populele.SetFret(string, fret, self._populele.LED_ON)

  def _setChord(self, chord):
    self._populele.SetAll(self._populele.LED_OFF)
    for fret in chord.getFrets():
        self._SetFret(fret[0], fret[1])

  def nextChord(self):
      self.song.nextChord()
      self.draw()

  def prevChord(self):
      self.song.prevChord()
      self.draw()

  def setSong(self, song):
    self.song = song
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

