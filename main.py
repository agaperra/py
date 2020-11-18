from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
import cv2
import numpy as np
from PIL import Image, ImageDraw
import os
import sqlite3
import time


# кодирование
def binary_pict(pic: str) -> str:
    with open(pic, 'rb') as f:
        binarr = enc64(f.read())  # b'iVBORw0KGgoAAAANSUhEUgAAAJE
    return binarr


# декодирование
def export(binary):
    # print(binary)
    image = BytesIO(dec64(binary))  # <_io.BytesIO object at 0x0000000002966708>
    #print(image)
    #pillow = Image.open(image)
    #x = pillow.show()


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


def count_substitutions(s1, s2):
    return sum(x != y for (x, y) in zip(s1, s2))


def createTable(db: str, table: str, column: str):
    connect = sqlite3.connect(db)
    curs = connect.cursor()
    curs.execute(str("""CREATE TABLE if not exists """ + table + """ (""" + column + """)"""))
    connect.commit()


def dropTable(db: str, table: str):
    connect = sqlite3.connect(db)
    curs = connect.cursor()
    curs.execute(str("""drop table if exists """ + table))
    connect.commit()


def insert(db: str, table: str, col: str, values: str):
    connect = sqlite3.connect(db)
    curs = connect.cursor()
    string_db = """INSERT INTO """ + table + """ (""" + col + """) VALUES (""" + values + """);"""
    curs.execute(string_db)
    connect.commit()


def select(db: str, table: str, col: str, values: str) -> str:
    connect = sqlite3.connect(db)
    curs = connect.cursor()
    a = curs.execute("""SELECT """ + col + """ from """ + table + """ where """ + values + """;""").fetchall()
    connect.commit()
    return a


def createByte(a: str):
    a = a[:0] + a[9:]
    a = a[:len(a) - 7] + a[len(a):]
    a = a[:len(a) - 2] + a[len(a):]
    a = a.encode()
    return a


# --------------------------------------------------------------------------------------------------------


start_time = time.time()
createTable("test.db", "data_pict", "id integer primary key autoincrement not null, code text not null")

for pack in files('.\\tst'):
    pict = 'tst\\' + pack
    picture = binary_pict(pict)
    temp = '"""' + "'" + str(picture) + "'" + '"""'
    insert("test.db", "data_pict", "code", temp)
    a = str(select("test.db", "data_pict", "code", "id=(select id from data_pict where code="+temp+")"))
    a = createByte(a)
    export(a)
print("--- %s seconds ---" % (time.time() - start_time))


