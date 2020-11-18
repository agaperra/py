from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
import cv2
import numpy as np
from PIL import Image, ImageDraw
import os
import time


# кодирование
def binary_pict(pic: str) -> str:
    with open(pic, 'rb') as f:
        binar = enc64(f.read())  # b'iVBORw0KGgoAAAANSUhEUgAAAJE
    return binar


# декодирование
def export(binary):
    image = BytesIO(dec64(binary))  # <_io.BytesIO object at 0x0000000002966708>
    pillow = Image.open(image)
    x = pillow.show()


# преобразование в черно-белое изображение
def black_white_rerange(path: str):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray[gray < np.mean(gray)] = 0.
    gray[gray >= np.mean(gray)] = 255.
    print(gray.shape)
    img = np.stack((gray,) * 3, axis=-1)
    print(img.shape)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# перевод в картинку из 1 и 0
def one_zero_paint(path):
    img = Image.open(path)
    h = img.height
    w = img.width
    x = 0
    y = 0
    D = ''
    imago = []
    while y < h:
        for x in range(w):
            z = img.getpixel((x, y))
            if z == 0:
                D = D + "1"
            else:
                D = D + "0"
        # print(D)
        imago.append(D)
        D = ""
        y += 1

    name = os.path.splitext(path)[0]
    file = open(name + '.txt', 'w')
    for i in imago:
        file.write(i)
        file.write('\n')
    file.close()


def files(path: object):
    for packet in os.listdir(path):
        if os.path.isfile(os.path.join(path, packet)):
            yield packet


# pict = '000KfhLkJ2G.png'
# export(binary_pict(pict))
# black_white_rerange(r"instax_round.jpg")
start_time = time.time()
for pack in files('.\\training'):
    one_zero_paint('training\\'+pack)
print("--- %s seconds ---" % (time.time() - start_time))
