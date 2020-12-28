from song import Song
from song.chord import Chord

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


