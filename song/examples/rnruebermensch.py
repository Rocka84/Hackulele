from song import Song

class RnRUebermensch(Song):
    def __init__(self, chord_repo):
        super(RnRUebermensch, self).__init__(chord_repo)

        self.name = "R'n'R Uebermensch"
        self.bpm = 130
        self.elements = [
                self._createElement("Am7", 4),
                self._createElement("Em", 4),
                self._createElement("F", 4),
                self._createElement("G", 4),
              ]
        self.reset()

