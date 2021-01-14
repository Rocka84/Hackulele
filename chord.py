
class Chord():
    def __init__(self, name, frets):
        self.name = name
        self.frets = frets

    def getName(self):
        return self.name

    def getFrets(self):
        return self.frets

    def __str__(self):
        return self.name

