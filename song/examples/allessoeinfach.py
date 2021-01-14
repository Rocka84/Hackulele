from song import Song

class AllesSoEinfach(Song):
    def __init__(self, chord_repo):
        super(AllesSoEinfach, self).__init__(chord_repo)

        self.name = "Alles so einfach"
        self.bpm = 140
        self.elements = [
                # Intro
                self._createElement("C", 4),
                self._createElement("Am", 4),
                self._createElement("Dm", 4),
                self._createElement("G", 4),

                self._createElement("C", 4),
                self._createElement("Am", 4),
                self._createElement("Dm", 4),
                self._createElement("G", 4),

                # Strophe
                self._createElement("Am", 4),
                self._createElement("Em", 4),
                self._createElement("F", 4),
                self._createElement("G", 4),

                self._createElement("Am", 4),
                self._createElement("Em", 4),
                self._createElement("F", 4),
                self._createElement("G", 4),

                self._createElement("F", 4),
                self._createElement("G", 4),
                self._createElement("C", 4),
                self._createElement("E", 4),

                self._createElement("F", 8),
                self._createElement("G", 4),


                self._createElement("G", 1),
                # refrain
                self._createElement("0", 3),

                self._createElement("C", 4),
                self._createElement("Em", 4),
                self._createElement("B", 4),
                self._createElement("F", 4),

                self._createElement("C", 4),
                self._createElement("Em", 4),
                self._createElement("B", 4),
                self._createElement("F", 4),

                self._createElement("C", 8),
                self._createElement("Am", 8),
                self._createElement("F", 8),
                self._createElement("G", 8),
              ]
        self.reset()


