from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO
import sqlite3

import cv2
import numpy as np
from PIL import Image
import os



#
# # кодирование
# def binary_pict(pic: str):
#     with open(pic, 'rb') as f:
#         binary = enc64(f.read())
#     return binary
#
#
# # декодирование
# def export(binary):
#     # print(binary)
#     image = BytesIO(dec64(binary))  # <_io.BytesIO object at 0x0000000002966708>
#     print(image)
#     # pillow = Image.open(image)
#     # x = pillow.show()

# преобразование в черно-белое изображение
def black_white(path: str):
    image = cv2.imread(path)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey[grey < np.mean(grey)] = 0.
    grey[grey >= np.mean(grey)] = 255.
    print(grey.shape)
    image = np.stack((grey,) * 3, axis=-1)
    print(image.shape)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# def count_substitutions(s1, s2):
#     return sum(x != y for (x, y) in zip(s1, s2))


# def create_table(db: str, table: str, column: str):
#     connect = sqlite3.connect(db)
#     curs = connect.cursor()
#     curs.execute(str("""CREATE TABLE if not exists """ + table + """ (""" + column + """)"""))
#     connect.commit()
#
#
# def drop_table(db: str, table: str):
#     connect = sqlite3.connect(db)
#     curs = connect.cursor()
#     curs.execute(str("""drop table if exists """ + table))
#     connect.commit()
#
#
# def insert(db: str, table: str, col: str, values: str):
#     connect = sqlite3.connect(db)
#     curs = connect.cursor()
#     string_db = """INSERT INTO """ + table + """ (""" + col + """) VALUES (""" + values + """);"""
#     curs.execute(string_db)
#     connect.commit()


# def select(db: str, table: str, col: str, values: str):
#     connect = sqlite3.connect(db)
#     curs = connect.cursor()
#     a = curs.execute("""SELECT """ + col + """ from """ + table + """ where """ + values + """;""").fetchone()
#     connect.commit()
#     return a


def create_byte(a: str):
    a = a[:0] + a[4:]
    a = a[:len(a) - 3] + a[len(a):]
    a = a.encode()
    return a

#
# def full():
#     for pack in files('testing'):
#         pict = 'testing\\' + pack
#         picture = binary_pict(pict)
#         temp = '"""' + "'" + str(picture) + "'" + '"""'
#         if len(pack) == 13:
#             pack = pack[:0] + pack[5:]
#             pack = pack[:len(pack) - 7] + pack[len(pack):]
#         if len(pack) == 17:
#             pack = pack[:0] + pack[5:]
#             pack = pack[:len(pack) - 11] + pack[len(pack):]
#         class_id = select("test.db", "classes", "id", "class=" + "'" + pack + "'")[0]
#         code_id = select("test.db", "data_pict", "id", "code=" + temp)[0]
#         # print(str(class_id) + ", " + str(code_id))
#         tmp = str(code_id) + "," + str(class_id)
#         insert("test.db", "pict_classes", "id_pict, id_class", tmp)

#
# def rows():
#     for pack in files('testing'):
#         pict = 'testing\\' + pack
#         picture = binary_pict(pict)
#         temp = '"""' + "'" + str(picture) + "'" + '"""'
#         insert("test.db", "data_pict", "code", temp)


# def class_insert():
#     connect = sqlite3.connect("test.db")
#     curs = connect.cursor()
#     classes = ['0',
#                '1',
#                '2',
#                '3',
#                '4',
#                '5',
#                '6',
#                '7',
#                '8',
#                '9',
#                'а',
#                'б',
#                'в',
#                'г',
#                'д',
#                'е',
#                'ж',
#                'з',
#                'и',
#                'й',
#                'к',
#                'л',
#                'м',
#                'н',
#                'о',
#                'п',
#                'р',
#                'с',
#                'т',
#                'у',
#                'ф',
#                'х',
#                'ц',
#                'ч',
#                'ш',
#                'щ',
#                'ъ',
#                'ы',
#                'ь',
#                'э',
#                'ю',
#                'я',
#                'А',
#                'Б',
#                'В',
#                'Г',
#                'Д',
#                'Е',
#                'Ж',
#                'З',
#                'И',
#                'Й',
#                'К',
#                'Л',
#                'М',
#                'Н',
#                'О',
#                'П',
#                'Р',
#                'С',
#                'Т',
#                'У',
#                'Ф',
#                'Х',
#                'Ц',
#                'Ч',
#                'Ш',
#                'Щ',
#                'Э',
#                'Ю',
#                'Я']
#     curs.executemany("INSERT INTO classes (class) VALUES (?)", classes)
#     connect.commit()


# one_zero_paint(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\1-char lower training\а\0043_а_02.png")
# createTable("test.db", "data_pict", "id integer primary key autoincrement not null, code text not null")
# createTable("test.db", "classes", " id    INTEGER     PRIMARY KEY AUTOINCREMENT NOT NULL, class VARCHAR (1) NOT NULL")
# createTable("test.db", "pict_classes",
#            "id_pict  INTEGER REFERENCES data_pict (id) NOT NULL, id_class INTEGER REFERENCES classes (id) NOT NULL")
#
# rows()
# classInsert()
# full()


# преобразование всех чисел во фрейме в тип float
# cols = dataframe.select_dtypes(exclude=['float']).columns
# dataframe[cols] = dataframe[cols].apply(pd.to_numeric, downcast='float', errors='coerce')
# print(dataframe)