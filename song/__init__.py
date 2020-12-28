
class Song(object):
    def __init__(self):
        self.bpm = 100
        self.current_chord = 0

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


