from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
import cv2
import numpy as np
from PIL import Image
import os
import sqlite3
import time
import pandas as pd
import xlrd


# кодирование
def binary_pict(pic: str):
    with open(pic, 'rb') as f:
        binarr = enc64(f.read())  # b'iVBORw0KGgoAAAANSUhEUgAAAJE
    return binarr


# декодирование
def export(binary):
    # print(binary)
    image = BytesIO(dec64(binary))  # <_io.BytesIO object at 0x0000000002966708>
    print(image)
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


def select(db: str, table: str, col: str, values: str):
    connect = sqlite3.connect(db)
    curs = connect.cursor()
    a = curs.execute("""SELECT """ + col + """ from """ + table + """ where """ + values + """;""").fetchone()
    connect.commit()
    return a


def createByte(a: str):
    a = a[:0] + a[4:]
    a = a[:len(a) - 3] + a[len(a):]
    a = a.encode()
    return a


def full():
    for pack in files('testing'):
        pict = 'testing\\' + pack
        picture = binary_pict(pict)
        temp = '"""' + "'" + str(picture) + "'" + '"""'
        if (len(pack) == 13):
            pack = pack[:0] + pack[5:]
            pack = pack[:len(pack) - 7] + pack[len(pack):]
        if (len(pack) == 17):
            pack = pack[:0] + pack[5:]
            pack = pack[:len(pack) - 11] + pack[len(pack):]
        class_id = select("test.db", "classes", "id", "class=" + "'" + pack + "'")[0]
        code_id = select("test.db", "data_pict", "id", "code=" + temp)[0]
        # print(str(class_id) + ", " + str(code_id))
        tmp = str(code_id) + "," + str(class_id)
        insert("test.db", "pict_classes", "id_pict, id_class", tmp)


def rows():
    for pack in files('testing'):
        pict = 'testing\\' + pack
        picture = binary_pict(pict)
        temp = '"""' + "'" + str(picture) + "'" + '"""'
        insert("test.db", "data_pict", "code", temp)


def classInsert():
    connect = sqlite3.connect("test.db")
    curs = connect.cursor()
    classes = [('0'),
               ('1'),
               ('2'),
               ('3'),
               ('4'),
               ('5'),
               ('6'),
               ('7'),
               ('8'),
               ('9'),
               ('а'),
               ('б'),
               ('в'),
               ('г'),
               ('д'),
               ('е'),
               ('ж'),
               ('з'),
               ('и'),
               ('й'),
               ('к'),
               ('л'),
               ('м'),
               ('н'),
               ('о'),
               ('п'),
               ('р'),
               ('с'),
               ('т'),
               ('у'),
               ('ф'),
               ('х'),
               ('ц'),
               ('ч'),
               ('ш'),
               ('щ'),
               ('ъ'),
               ('ы'),
               ('ь'),
               ('э'),
               ('ю'),
               ('я'),
               ('А'),
               ('Б'),
               ('В'),
               ('Г'),
               ('Д'),
               ('Е'),
               ('Ж'),
               ('З'),
               ('И'),
               ('Й'),
               ('К'),
               ('Л'),
               ('М'),
               ('Н'),
               ('О'),
               ('П'),
               ('Р'),
               ('С'),
               ('Т'),
               ('У'),
               ('Ф'),
               ('Х'),
               ('Ц'),
               ('Ч'),
               ('Ш'),
               ('Щ'),
               ('Э'),
               ('Ю'),
               ('Я')]
    curs.executemany("INSERT INTO classes (class) VALUES (?)", classes)
    connect.commit()


# --------------------------------------------------------------------------------------------------------


createTable("test.db", "data_pict", "id integer primary key autoincrement not null, code text not null")
createTable("test.db", "classes", " id    INTEGER     PRIMARY KEY AUTOINCREMENT NOT NULL, class VARCHAR (1) NOT NULL")
createTable("test.db", "pict_classes",
            "id_pict  INTEGER REFERENCES data_pict (id) NOT NULL, id_class INTEGER REFERENCES classes (id) NOT NULL")
#
# rows()
# classInsert()
# full()



