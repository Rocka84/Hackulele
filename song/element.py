from chord import Chord

class Element():
    def __init__(self, chord, duration):
        self.chord = chord
        self.duration = duration

    def getChord(self):
        return self.chord

    def getDuration(self):
        return self.duration

    def __str__(self):
        return "%-4s  x%i" % ( self.chord, self.duration )
