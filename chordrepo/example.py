from chordrepo import ChordRepo
from chord import Chord

class ExampleChordRepo(ChordRepo):
    CHORDS = {
            "0":   Chord("0",   [ [0,0], [0,0], [0,0], [0,0] ]),

            "C":   Chord("C",   [ [3,3], [0,0], [0,0], [0,0] ]),
            "D":   Chord("D",   [ [0,0], [0,0], [0,0], [0,0] ]),
            "Dm":  Chord("Dm",  [ [0,0], [1,1], [2,3], [2,2] ]),
            "E":   Chord("E",   [ [2,1], [4,4], [4,3], [4,2] ]),
            "Em":  Chord("Em",  [ [2,1], [3,2], [4,3], [0,0] ]),
            "F":   Chord("F",   [ [0,0], [1,1], [0,0], [2,2] ]),
            "G":   Chord("G",   [ [2,1], [3,3], [2,1], [0,0] ]),
            "Am":  Chord("Am",  [ [0,0], [0,0], [0,0], [2,2] ]),
            "Am7": Chord("Am7", [ [3,3], [0,0], [0,0], [2,2] ]),
            "B":   Chord("B",   [ [1,1], [1,1], [2,2], [3,3] ]),
        }

    def getChord(self, chord_name):
        if chord_name not in self.CHORDS:
            return self.CHORDS["0"]
        return self.CHORDS[chord_name]

