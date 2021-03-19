from father import Father
from mother import Mother


class Child(Father, Mother):
    def __init__(self, money, face_value):

        Father.__init__(self, money)
        Mother.__init__(self, face_value)
