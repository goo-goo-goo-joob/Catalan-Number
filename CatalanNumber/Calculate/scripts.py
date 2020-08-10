from PIL import Image, ImageDraw, ImageFont
import math
import platform
import subprocess


def polygon(brackets, name, choice):
    # brackets = "(()())"
    l = 300  # длина ребра
    p = 50  # отступ
    r = 40  # радиус круга
    outline = 3  # толщина круга
    set = 10  # отступ цифр
    font = ImageFont.truetype("arial.ttf", 40)
    n = len(brackets) / 2 + 2  # кол-во вершин
    R = l / (2 * math.sin(math.pi / n))
    img = Image.new('RGB', (int(R + p) * 2 + 1, int(R + p) * 2 + 1), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    center = [R + p, R + p]
    coord = []
    for i in range(0, int(n)):
        alph = 2 * math.pi * i / n - math.pi / n  # угол поворота
        row = [R + p + R * math.sin(alph), R + p + R * math.cos(alph)]
        coord.append(row)
        draw.line((coord[i - 1][0], coord[i - 1][1], coord[i][0], coord[i][1]), fill=0, width=4)
    draw.line((coord[0][0], coord[0][1], coord[i][0], coord[i][1]), fill=0, width=4)
    draw.line((coord[0][0], coord[0][1], coord[1][0], coord[1][1]), fill=127, width=5)
    partition(draw, coord, brackets, int(n), 0, 1)
    for i in range(0, int(n)):
        draw.ellipse((coord[i][0] - r - outline, coord[i][1] - r - outline, coord[i][0] + r + outline, coord[i][1] + r + outline), fill='black')
        draw.ellipse((coord[i][0] - r, coord[i][1] - r, coord[i][0] + r, coord[i][1] + r), fill='white')
        if choice:
            if (i + 1) > 9:
                set = 23
            draw.text((coord[i][0] - set, coord[i][1] - 20), '%d' % (i + 1), fill="black", font=font)
    del draw
    img = img.resize((int(R + p) + 1, int(R + p) + 1), Image.ANTIALIAS)
    img.save(name, subsampling=0, quality=100)
    return 0


def get(brackets):
    i = j = 0
    while True:
        if brackets[i] != 0:
            if brackets[i] == '(':
                j += 1
            else:
                j -= 1
            i += 1
        if j == 0:
            break
    return i  # кол-во скобок внутри левой части


def partition(draw, coord, brackets, n, a, b):
    left = int(get(brackets) / 2 + 1)
    right = int(n - left + 1)
    if left > 2:
        draw.line((coord[a][0], coord[a][1], coord[b + right - 1][0], coord[b + right - 1][1]), fill=0, width=3)
        br = brackets[1: 2 * (left - 2) + 1]
        partition(draw, coord, br, left, a, (b + right - 1))
    if right > 2:
        draw.line((coord[b][0], coord[b][1], coord[b + right - 1][0], coord[b + right - 1][1]), fill=0, width=3)
        br = brackets[2 * (left - 2) + 2:]
        if b == 0 or b > (b + right - 1):
            partition(draw, coord, br, right, b, (b + right - 1))
        else:
            partition(draw, coord, br, right, (b + right - 1), b)
    pass


def check(brackets):
    if len(brackets) > 80:
        return 4
    j = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            j += 1
        elif brackets[i] == ')':
            j -= 1
        else:
            return 2
        if j < 0:
            return 1
    if j != 0:
        return 1
    return 0


def callPolygon(brackets, name, numbering):
    if platform.system() == 'Linux':
        return polygon(brackets, name, numbering)
    else:
        return polygon(brackets, 'Calculate/' + name, numbering)


def callBinTree(brackets, name, numbering):
    if numbering:
        if platform.system() == 'Linux':
            return subprocess.call(['./Cat_Br_Tr_Num.o', brackets, name])
        else:
            return subprocess.call(['Cat_Br_Tr_Num.exe', brackets, 'Calculate/' + name])
    else:
        if platform.system() == 'Linux':
            return subprocess.call(['./Cat_Br_Tr.o', brackets, name])
        else:
            return subprocess.call(['Cat_Br_Tr.exe', brackets, 'Calculate/' + name])


def callRootTree(brackets, name, numbering):
    if numbering:
        if platform.system() == 'Linux':
            return subprocess.call(['./Cat_Tree_Win_Num.o', brackets, name])
        else:
            return subprocess.call(['Cat_Tree_Win_Num.exe', brackets, 'Calculate/' + name])
    else:
        if platform.system() == 'Linux':
            return subprocess.call(['./Cat_Tree_Win.o', brackets, name])
        else:
            return subprocess.call(['Cat_Tree_Win.exe', brackets, 'Calculate/' + name])


def callTableJung(brackets, name):
    if platform.system() == 'Linux':
        return subprocess.call(['./Cat_Jung.o', brackets, name])
    else:
        return subprocess.call(['Cat_Jung.exe', brackets, 'Calculate/' + name])
