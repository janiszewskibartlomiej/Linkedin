# Bartłomiej Janiszewski

from random import sample

class TaliaKart:
    def __init__(self):

        self._karty = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
                       '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
                       '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
                       'J♦', 'Q♦', 'K♦', 'A♦']

    def __next__(self):

        if self._karty == []:
            raise StopIteration

        cart = sample(self._karty, k=1)

        for index, symbol in enumerate(self._karty):

            if symbol == cart:
                self._karty.remove(self._karty[index])

        return cart

    def __iter__(self):
        return self


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    a1 = TaliaKart()
    print(a1)
    pass

