JUMP = 2


class Notes:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self):
        self._value = self._value * JUMP


class MusicNotes:
    def __init__(self):
        self._notes = []
        self._index = -1
        self._column = 0

    def add_note(self, new_note):
        self._notes.append(new_note)

    def __iter__(self):
        return self

    def __next__(self):
        print("-----")
        print("column=" + str(self._column))
        print("index=" + str(self._index))

        if self._column > 5:
            raise StopIteration()

        if self._index > 4:
            self._index = 0
            self._column += 1
        else:
            self._index += 1

        print("column=" + str(self._column))
        print("index=" + str(self._index))
        result = self._notes[self._index].get_value()
        self._notes[self._index].set_value()

        return result


MN = MusicNotes()
MN.add_note(Notes("La", 55))
MN.add_note(Notes("Si", 61.74))
MN.add_note(Notes("Do", 65.41))
MN.add_note(Notes("Re", 73.42))
MN.add_note(Notes("Mi", 82.41))
MN.add_note(Notes("Fa", 87.31))
MN.add_note(Notes("Sol", 98))

notes_iter = iter(MN)
for freq in notes_iter:
    print("frequency: " + str(freq))
