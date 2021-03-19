class Card(object):
    def __init__(self, card_id, card_passwd, card_money):
        self.card_id = card_id
        self.card_passwd = card_passwd
        self.card_money = card_money
        self.card_lock = False
