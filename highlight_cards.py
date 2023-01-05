import cv2
from detect_cards import input_image_path
img = cv2.imread(input_image_path)

f = open("set_cards_list.txt", "r")
test_cards = []
test_cards = f.readlines()
f.close()

# print(test_cards)
for z in range(3):
    card = test_cards[z][8:]  # sliced format: x-y_w-h.jpg
    i = 0
    x, y, w, h = '', '', '', ''

    while card[i] != '-':
        x += card[i]
        i += 1
    else:
        i += 1
        while card[i] != '_':
            y += card[i]
            i += 1
        else:
            i += 1
            while card[i] != '-':
                w += card[i]
                i += 1
            else:
                i += 1
                while card[i] != '.':
                    h += card[i]
                    i += 1
                else:
                    pass
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('test', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
