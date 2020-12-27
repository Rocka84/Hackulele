"""Animator for Song effect."""

import random

from animations import Animator

class SongAnimator(Animator):
  """Animator for a Song."""

  def __init__(self, *args, **kwargs):
    """Initializes a SongAnimator object."""
    super(SongAnimator, self).__init__(*args, **kwargs)

    # self.song = RnRUebermensch()
    self.song = AllesSoEinfach()
    self.interval = 60000 / self.song.getBPM()

  def _SetFret(self, string, fret):
    self._populele.SetPixel(self._populele.NB_COLS - fret, string - 1, self._populele.LED_ON)

  def _setChord(self, chord):
    self._populele.SetAll(self._populele.LED_OFF)
    for fret in chord.getFrets():
        self._SetFret(fret[0], fret[1])


  def Draw(self):
    self.song.beat()
    self._setChord(self.song.getCurrentChord())
    print(self.song.getCurrentChord().getName())


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

    def beat(self):
        if self.current_duration == 0:
            self.current_chord += 1
            if self.current_chord == len(self.chords):
                self.current_chord = 0
            self.current_duration = self.getChord(self.current_chord).getDuration()
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
