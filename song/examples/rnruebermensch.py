from song import Song
from song.chord import Chord

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

