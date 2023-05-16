class Card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        self.omote = f'img/{self.suit}{self.number}.png'

    def print_card(self):
        print(self.suit,self.number)


if __name__ == '__main__':
    c1 = card('heart',1)
    c1.print_card()
