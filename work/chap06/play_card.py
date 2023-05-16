from card import Card
import random

stock = []

for s in ['heart','diamond','club','spade']:
    for n in range(1,14):
        card = Card(s,n)
        card.print_card()
        stock.append(card)

random.shuffle(stock)
i = random.randint(1, len(stock)) -1
card = stock[i]
del stock[i]
card.print_card()
print(card.omote)
print('--------------------------')

print('残り:',len(stock))

for c in stock:
    c.print_card
