import numpy
from PIL import Image
import os
import openpyxl
import pandas as pd


# перевод в картинку из 1 и 0
def one_zero_paint(path):
    image = Image.open(path)
    height = image.height
    width = image.width
    y_coord = 0
    D = ""
    imago = []
    while y_coord < height:
        for x_coord in range(width):
            z = image.getpixel((x_coord, y_coord))
            if z == 0:
                D = D + "1"
            else:
                D = D + "0"
        imago.append(D)
        D = ""
        y_coord += 1

    name = os.path.splitext(path)[0]
    file = open(name + '.txt', 'w')
    for i in imago:
        file.write(i)
        file.write('\n')
    file.close()


def files(path):
    for packet in os.listdir(path):
        if os.path.isfile(os.path.join(path, packet)):
            yield packet


def find_one(mat):
    z = 0
    for k in range(len(mat)):
        for j in range(len(mat[k])):
            if mat[k][j] == "1":
                z = z + 1
    return z


def find_parameters(matr):
    x = numpy.array(matr)
    counter = []
    for u in range(0, 5):
        for w in range(0, 5):
            matrix_B = x[u * 29:(u + 1) * 29, w * 29:(w + 1) * 29].copy()
            m = find_one(matrix_B)
            counter.append(m)
    return counter


# --------------------------------------------------------------------------------------------------------
# перевод набора в текстовые файлы
# for file_ in files(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\png"):
#     one_zero_paint(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\png\\"+file_)

# построение подматриц
wb = openpyxl.Workbook()
ws = wb.active
global_matrix = []
array = []
for i in range(1, 27):
    array.append("param " + str(i))
global_matrix.append(array)
for file_ in files(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\txt"):
    matrix = []
    count = []
    with open(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\txt\\" + file_) as fin:
        line1 = fin.readline()
        for line in fin:
            matrix.append(list(line))
        count = find_parameters(matrix)
    count.append(file_[5])
    global_matrix.append(list(count))
for subarray in global_matrix:
    ws.append(subarray)
wb.save(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\test.xlsx")

# загрузка данных из excel
dataframe = pd.read_excel(r"F:\agaperra\МЭИ\Мага\ВКР\begin\рукопись_dig_char\pr\train\test.xlsx", )
print(dataframe)
