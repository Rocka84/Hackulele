from __future__ import print_function
import time

class Player():
  """Animator for a Song."""

  def __init__(self, populele, song = None):
    self._populele = populele
    self.song = AllesSoEinfach() if song == None else song
    self.interval = 60.0 / self.song.getBPM()

  def _SetFret(self, string, fret):
    self._populele.SetPixel(self._populele.NB_COLS - fret, string - 1, self._populele.LED_ON)

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


class Song(object):
    def __init__(self):
        self.bpm = 100
        self.current_chord = 0
        # self.current_duration = self.getChord(0).getDuration()

    def getBPM(self):
        return self.bpm

    def getChord(self, index):
        return self.chords[index]

    def getCurrentChord(self):
        return self.chords[self.current_chord]

    def nextChord(self):
        self.current_chord += 1
        if self.current_chord == len(self.chords):
            self.current_chord = 0
        self.current_duration = self.getChord(self.current_chord).getDuration()

    def prevChord(self):
        self.current_chord -= 1
        if self.current_chord < 0:
            self.current_chord = len(self.chords) - 1
        self.current_duration = self.getChord(self.current_chord).getDuration()

    def reset(self):
        self.current_chord = 0
        self.current_duration = self.getChord(self.current_chord).getDuration()

    def beat(self):
        if self.current_duration == 0:
            self.nextChord()
        self.current_duration -= 1


class Chord():
    def __init__(self, name, frets, duration = 1):
        self.name = name
        self.frets = frets
        self.duration = duration

    def getName(self):
        return self.name

    def getFrets(self):
        return self.frets

    def getDuration(self):
        return self.duration

    def __str__(self):
        return "%-4s  x%i" % ( self.name, self.duration )

class TestSong(Song):
    def __init__(self):
        super(TestSong, self)
        self.chords = [
                Chord("C", [ [1,3] ], 4),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),
                Chord("Am", [ [4,2] ], 4),
                Chord("F", [ [2,1], [4,2] ], 4),
              ]

        self.bpm = 100
        self.current_chord = 0
        self.current_duration = self.getChord(0).getDuration()

class RnRUebermensch(Song):
    def __init__(self):
        super(RnRUebermensch, self)
        self.chords = [
                Chord("Am7", [ [4,2], [1,3] ], 4),
                Chord("Em", [ [1,2], [2,3], [3,4] ], 4),
                Chord("F", [ [2,1], [4,2] ], 4),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),
              ]

        self.bpm = 100
        self.current_chord = 0
        self.current_duration = self.getChord(0).getDuration()

class AllesSoEinfach(Song):
    def __init__(self):
        super(AllesSoEinfach, self)
        self.chords = [
                Chord("Am", [ [4,2] ], 4),
                Chord("Em", [ [1,2], [2,3], [3,4] ], 4),
                Chord("F", [ [2,1], [4,2] ], 4),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),

                Chord("Am", [ [4,2] ], 4),
                Chord("Em", [ [1,2], [2,3], [3,4] ], 4),
                Chord("F", [ [2,1], [4,2] ], 4),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),

                Chord("F", [ [2,1], [4,2] ], 4),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),
                Chord("C", [ [1,3] ], 4),
                Chord("E", [ [1,2], [2,4], [3,4], [4,4] ], 4),

                Chord("F", [ [2,1], [4,2] ], 8),
                Chord("G", [ [1,2], [2,3], [3,2] ], 4),
              ]

        self.bpm = 100
        self.current_chord = 0
        self.current_duration = self.getChord(0).getDuration()
