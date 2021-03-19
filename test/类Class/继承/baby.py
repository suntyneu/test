from baba import Baba
from mam import Mam


class Baby(Baba, Mam):
    def __init__(self, money, nice, work, sing):
        Baba.__init__(self, sing)
        Mam.__init__(self, nice)
        Mam.work(self, work)
        Baba.money(self, money)
