class Card:
    def __init__(self, color, shading, shape, number):
        self.color = color
        self.shading = shading
        self.shape = shape
        self.number = number


card1 = Card('', '', '', '')
filename = "p-e-d-2.PNG"

i = 0
features = {'r': 'red', 'g': 'green', 'p' : 'purple', 'f' : 'full', 'l' : 'lines', 'e' : 'empty', 'o' : 'oval',
            'd' : 'diamond', 's' : 'squiggly', '1' : 'one', '2' : 'two', '3' : 'three'}
try:
    card1.number = features[filename[i]]
    i += 1
except KeyError as e:
    i += 1
print(card1.color, card1.shading, card1.shape, card1.number)