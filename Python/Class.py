#defining class
class students:
    def __init__(self,marks):
        # self.name = name
        # self.faculty = faculty
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,new_marks):
        if new_marks < 80:
            print("Not Enough Marks")
        else:
            self._marks = new_marks

s = students(10)
print(s._marks)


