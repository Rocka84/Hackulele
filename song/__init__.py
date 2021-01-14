from song.element import Element

class Song(object):
    def __init__(self, chordrepo):
        self.bpm = 100
        self.current_element = 0
        self.chordrepo = chordrepo
        self.name = "unknown"

    def getBPM(self):
        return self.bpm

    def getName(self):
        return self.name

    def getCurrentElement(self):
        return self.elements[self.current_element]

    def getCurrentChord(self):
        return self.getCurrentElement().getChord()

    def nextElement(self):
        self.current_element += 1
        if self.current_element == len(self.elements):
            self.current_element = 0
        self.current_duration = self.getCurrentElement().getDuration()

    def prevElement(self):
        if self.current_duration == self.getCurrentElement().getDuration():
            self.current_element -= 1
            if self.current_element < 0:
                self.current_element = len(self.elements) - 1
        self.current_duration = self.getCurrentElement().getDuration()

    def reset(self):
        self.current_element = 0
        self.current_duration = self.getCurrentElement().getDuration()

    def beat(self):
        if self.current_duration == 0:
            self.nextElement()
        self.current_duration -= 1

    def _createElement(self, chord_name, duration):
        return Element(
                self.chordrepo.getChord(chord_name),
                duration
            )

