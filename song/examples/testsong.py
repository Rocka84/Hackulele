from song import Song

class TestSong(Song):
    def __init__(self, chord_repo):
        super(TestSong, self).__init__(chord_repo)

        self.name = "TestSong"
        self.bpm = 100
        self.elements = [
                self._createElement("C", 4),
                self._createElement("G", 4),
                self._createElement("Am", 4),
                self._createElement("F", 4),
              ]
        self.reset()


