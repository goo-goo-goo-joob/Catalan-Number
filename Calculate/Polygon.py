from PIL import Image, ImageDraw, ImageFont
import math
brackets = "()"
l = 100 #длина ребра
p = 30 #отступ
n = len(brackets)/2+2 #кол-во вершин
R = l/(2*math.sin(math.pi/n))
img = Image.new('RGB', (int(R+p)*2+1, int(R+p)*2+1), (255, 255, 255))
draw = ImageDraw.Draw(img)
center=[R+p, R+p]
coord = []
row = [R+p,2*R+p]
coord.append(row)
for i in range(1, int(n)):
    alph = 2*math.pi*i/n #угол поворота
    row = [R+p+R*math.sin(alph),R+p+R*math.cos(alph)]
    coord.append(row)
    draw.line((coord[i-1][0], coord[i-1][1],coord[i][0], coord[i][1]),fill=0, width=3)
draw.line((coord[0][0], coord[0][1],coord[i][0], coord[i][1]),fill=0, width=3)

def get(brackets):
    i = j =0
    while True:
        if (brackets[i] != 0):
            if (brackets[i] == '('):
                j+=1
            else: j-=1
            i+=1
        if (j==0):
            break
    return i #кол-во скобок внутри левой части

def partition(brackets, n, a, b):
    left = get(brackets)/2+1
    right = n - left + 1
    if (left>2):
        draw.line((coord[b][0], coord[b][1],coord[b + right - 1][0], coord[b + right - 1][1]),fill=0, width=3)
        br = brackets[1: 2 * (left - 2)+1]
        partition(br, left, a, (b + right - 1))
    if (right>2):
        draw.line((coord[a][0], coord[a][1],coord[b + right - 1][0], coord[b + right - 1][1]),fill=0, width=3)
        br = brackets[2 * (left - 2)+2:]
        if(b ==1 or b>(b + right - 1)):
            partition(br, right, b, (b + right - 1))
        else: partition(br, right, (b + right - 1), b)
    pass

partition(brackets,n,0,1)
del draw
img.save("polygon.png")