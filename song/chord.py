
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

