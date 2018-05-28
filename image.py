from PIL import Image
import numpy
import time


init = [
    [True, True, True, False, False, False, False, True, True,
     True, True, False, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     False, False, True, False, False, True, True, True, True,
     True, True, False, False, False, False, True, True, True,
     True, True, True, False, False, False, False, True, True,
     True, True, True, True, False, False, False, False, True,
     True, True, True, True, False, False, False, True, False,
     False, True, True, True, True, False, False, False, True,
     False, False, False, False, False, False, False, False, False,
     True, True, True, False, False, False, False, True, False,
     False, True, True, True, True, True, True, True, True,
     False, False, True, False, True, True, True, True, True,
     False, False, False, False, False, False, True, True, True,
     False, False, False, True, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, True, True, True],
    [True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True],
    [True, True, True, False, False, False, False, False, True,
     True, True, True, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     False, False, True, True, False, False, True, True, True,
     True, False, False, True, True, False, False, True, True,
     True, True, False, False, True, True, False, False, False,
     True, True, True, False, False, True, True, True, False,
     False, False, False, False, False, True, True, True, True,
     False, False, False, False, False, False, False, True, True,
     False, False, True, True, True, True, False, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, True,
     False, False, False, False, True, True, True, True, True,
     True, False, False, False, False, False, True, True, True,
     True, False, False, False, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, False, True, True],
    [True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     False, False, False, False, False, False, False, False, False,
     False, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True],
    [True, True, True, False, False, False, False, True, True,
     True, True, True, False, False, False, False, False, False,
     True, True, True, False, False, True, True, True, False,
     False, False, True, True, False, False, True, True, True,
     True, False, False, True, False, False, True, True, True,
     True, True, True, False, False, False, False, True, True,
     True, True, True, True, False, False, False, False, True,
     True, True, True, True, True, False, False, False, False,
     True, True, True, True, True, True, False, False, False,
     False, True, True, True, True, True, True, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, False,
     False, False, True, False, False, True, True, True, True,
     False, False, True, True, False, False, False, True, True,
     False, False, False, True, True, True, False, False, False,
     False, False, False, True, True, True, True, True, False,
     False, False, False, True, True, True],
    [True, True, True, False, False, False, False, False, True,
     True, True, True, False, False, False, False, False, False,
     False, True, True, False, False, False, True, True, True,
     False, False, False, True, False, False, True, True, True,
     True, True, False, False, False, False, True, True, True,
     True, True, True, True, True, False, False, True, False,
     False, False, False, True, True, True, False, False, False,
     False, False, False, False, False, False, True, False, False,
     False, True, True, True, True, False, False, True, False,
     False, False, True, True, True, True, True, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, True,
     False, False, False, False, True, True, True, True, True,
     True, False, False, True, False, False, True, True, True,
     True, False, False, True, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, False, True, True],
    [True, True, False, False, False, False, False, False, True,
     True, True, False, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     False, False, True, False, False, True, True, True, True,
     True, True, False, False, False, False, True, True, True,
     True, True, True, False, False, True, True, True, True,
     True, True, True, False, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True],
    [True, True, True, True, True, True, False, False, True,
     True, True, True, True, True, True, False, False, False,
     True, True, True, True, True, True, True, False, False,
     False, True, True, True, True, True, True, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, False,
     False, True, False, False, True, True, True, True, True,
     False, False, True, False, False, True, True, True, True,
     False, False, True, True, False, False, True, True, True,
     False, False, True, True, True, False, False, True, True,
     True, False, False, True, True, True, False, False, True,
     True, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, True, True, True, True, True, True,
     False, False, True, True, True, True, True, True, True,
     True, False, False, True, True, True, True, True, True,
     True, True, False, False, True, True],
    [True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, False, False, True,
     True, True, True, True, True, True, True, False, False,
     True, True, True, True, True, True, True, True, False,
     False, True, True, True, True, True, True, True, True,
     False, False, True, True, True, True, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, True,
     True, True, True, False, False, True, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, True, False, False, True, True,
     True, True, True, True, True, True, False, False, True,
     True, True, True, True, True, True, True, False, False,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True],
    [True, True, True, True, True, False, False, False, False,
     False, True, True, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, True, True, True,
     False, False, False, False, True, True, True, True, True,
     True, False, False, False, False, True, True, True, True,
     True, True, False, False, False, False, True, True, True,
     True, True, True, False, False, False, False, True, True,
     True, True, True, True, False, False, False, False, True,
     True, True, True, True, True, False, False, False, False,
     True, True, True, True, True, True, False, False, False,
     False, True, True, True, True, True, True, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, True,
     False, False, False, False, True, True, True, True, True,
     True, False, False, False, False, True, True, True, True,
     True, True, False, False, False, False],
    [True, False, False, False, False, False, False, False, False,
     True, True, False, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, True, False, False, True, True,
     True, True, True, True, True, True, False, False, False,
     False, False, False, True, True, True, True, False, False,
     False, False, False, False, False, True, True, True, False,
     False, True, True, True, True, False, False, True, True,
     False, True, True, True, True, True, False, False, False,
     True, True, True, True, True, True, True, True, False,
     False, True, True, True, True, True, True, True, True,
     False, False, True, False, True, True, True, True, True,
     False, False, False, False, False, False, True, True, True,
     True, False, False, True, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, True, True, True],
    [False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, True, True, True, True, True, True, True,
     False, False, False, True, True, True, True, True, True,
     True, False, False, True, True, True, True, True, True,
     True, False, False, False, True, True, True, True, True,
     True, True, False, False, True, True, True, True, True,
     True, True, False, False, False, True, True, True, True,
     True, True, True, False, False, True, True, True, True,
     True, True, True, False, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, True, False, False, True, True,
     True, True, True, True, True, False, False, True, True,
     True, True, True, True, True, False, False, False, True,
     True, True, True, True, True, True, False, False, True,
     True, True, True, True, True, True, True, False, False,
     True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True],
    [True, True, False, False, False, False, False, True, True,
     True, True, False, False, False, False, False, False, False,
     False, True, False, False, False, True, True, True, True,
     False, False, True, False, False, True, True, True, True,
     True, False, False, True, False, False, True, True, True,
     True, True, False, False, False, True, True, True, True,
     True, True, True, False, False, True, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, True, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, True, True,
     True, True, True, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False],
    [True, True, True, False, False, False, False, False, True,
     True, True, False, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     False, False, True, False, False, True, True, True, True,
     True, False, False, False, True, True, True, True, True,
     True, True, False, False, False, True, True, True, True,
     True, True, True, False, False, True, True, True, True,
     False, False, False, False, False, False, True, True, True,
     True, False, False, False, False, False, False, True, True,
     True, True, True, True, True, True, False, False, True,
     True, True, True, True, True, True, True, True, False,
     False, True, True, True, True, True, True, True, True,
     False, False, False, False, True, True, True, True, True,
     True, False, False, False, False, False, True, True, True,
     True, False, False, False, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, False, True, True],
    [True, True, True, False, False, False, False, False, True,
     True, True, True, False, False, False, False, False, False,
     False, True, True, False, False, True, True, True, True,
     False, False, True, True, False, False, True, True, True,
     True, True, False, False, False, False, True, True, True,
     True, True, True, True, True, False, False, True, False,
     False, False, False, True, True, True, False, False, False,
     False, False, False, False, False, True, True, False, False,
     False, True, True, True, True, False, False, True, False,
     False, True, True, True, True, True, False, False, False,
     False, False, True, True, True, True, True, True, False,
     False, False, False, True, True, True, True, True, True,
     False, False, False, False, True, True, True, True, True,
     False, False, False, True, False, False, True, True, True,
     True, False, False, True, True, False, False, False, False,
     False, False, False, False, True, True, True, False, False,
     False, False, False, True, True, True],
    [True, True, True, False, True, True, True, True, False, True, True, True,
     True, False, True, True, True, True, False, True, True, True, True, False,
     True, True, True, False, False, True, True, True, False, False, True, True,
     True, False, False, True, True, True, False, False, True, True, True, False,
     False, True, True, True, False, False, True, True, True, True, False, True,
     True, False, True, False, True, True, False, True, False, True, True, False,
     True, False, True, True, False, True, False, True, True, False, True, False,
     True, True, False, True, False, True, False, True, True, False, True, False,
     True, True, False, True, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False,
     True, True, True, False, True, True, True, True, False, True, True, True,
     True, False, True, True, True, True, False, True, True, True, True, False,
     True, True, True, True, False, True, ],
    [True, True, False, True, True, True, True, True, False, True, True, False,
     False, False, True, True, True, True, False, True, True, False, True, False,
     True, True, True, True, False, True, True, True, True, True, True, True,
     True, False, False, True, False, True, True, True, False, True, True, False,
     False, True, False, True, True, True, False, True, True, False, False, True,
     False, True, True, True, False, True, False, True, False, True, False, True,
     True, True, False, True, False, True, False, True, False, True, True, True,
     False, True, False, True, False, True, False, True, True, True, False, False,
     True, True, False, True, False, True, True, True, False, False, False, False,
     False, False, False, True, True, True, True, False, False, False, False, False,
     True, False, True, False, True, True, True, True, False, True, True, False,
     False, False, True, True, True, True, False, True, True, True, False, True,
     True, True, True, True, False, True, ]
]
init_pos = ['9', '-', '8', '=', '0', '6', '2', '=', '4', '+', '1', '5', '7', '=', '2', '3', '6', '44', '04']


# 初始化函数  将123..原型载入
def Init():
    j = 1
    while j <= 13:
        src = Image.open("E://python/untitled/加减大师作弊/venv/Images/" + str(j) + ".png")
        list1 = Cut(src)
        for i in list1:
            pos, resum, re_img = ImgHashRecognit(i)
            if resum == 55555555 or resum > 5:
                i.show()
                kk = input("Input this num:")

                init.append(numpy.array(re_img).flatten())
                init_pos.append(kk)
            print("与" + str(init_pos[pos]) + "的" + "汉明距离：" + str(resum))
        j = int(j) + 1

    print(init)
    print(init_pos)


def Cut(img):
    img = binarize(img)
    img1, img2 = HorCut(img)

    return AcrCut(img1) + AcrCut(img2)


def binarize(img, threshold=200):
    """图像二值化"""
    img = img.convert('L')

    table = []
    for i in range(256):
        if i > threshold:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')

    return bin_img


def ImgHashRecognit(img):
    re_img = img.resize((10, 15), Image.LANCZOS)

    hash_img = numpy.array(re_img).flatten()
    # print(hash_img)
    mpos = 0
    msum = 55555555  # 赋值大值
    # print(hash_img) 测试专用
    for i in range(len(init)):

        try:
            num = sum(k != j for k, j in
                      zip(init[i], hash_img))  # zip（a,b） 将其合并成((a[i],b[i]),(...))形式   sum将返回的a[i] b[i]个数
            if num < msum:
                mpos = i
                msum = num
        except:
            pass

    return mpos, msum, re_img


def AcrCut(img):
    li = list(numpy.sum(numpy.array(img) == 0, axis=0))  # 对每一列进行求和并返回一行元素
    k = 0

    posx = []
    width, height = img.size
    for i in range(len(li)):
        if i > 0 and li[i] >= 5 and li[i - 1] < 5:
            posx.append(i)
            k = k + 1
        if i > 0 and li[i - 1] >= 5 and li[i] < 5:
            posx.append(i)
            k = k + 1

    if len(posx) % 2 == 1:  # 没用的一句话
        posx.append(width)
    lis = []
    try:
        for i in range(len(posx)):  # 遍历寻找起始与结束点，数量不确定，所以用数组遍历
            if i % 2 == 0:
                lis.append(img.crop([posx[i], 0, posx[i + 1], height]))

        return lis

    except:

        print("Error in AcrCut")


def HorCut(img):
    li = list(numpy.sum(numpy.array(img) == 0, axis=1))  # 将其转换为array并求和
    k = 0
    posy = []
    for i in range(len(li)):
        if ((i > 0) and (li[i] >= 5) and (li[i - 1] < 5)):
            posy.append(i)
            k = k + 1
        if ((i > 0) and (li[i - 1] >= 5) and (li[i] < 5)):
            posy.append(i)
            k = k + 1

    if len(posy) == 4:
        width, height = img.size
        img_opertion = img.crop([0, posy[0], width, posy[1]])
        img_result = img.crop([0, posy[2], width, posy[3]])
        return img_opertion, img_result

    else:

        print("Error in HorCut")


def Result(src):
    list1 = Cut(src)
    shizi = []

    for i in list1:
        pos, resum, re_img = ImgHashRecognit(i)
        shizi.append(init_pos[pos])

        if resum == 55555555:
            print("Error")
            time.sleep(100)
            return False
    str1 = ""
    str2 = ""
    f = True
    for j in range(len(shizi)):
        print(shizi[j])
        if shizi[j] == '=':
            f = False
            continue

        if f:
            str1 = str1 + shizi[j]
        else:
            str2 = str2 + shizi[j]

    return eval(str1) == eval(str2)


# 调试所用
if __name__ == '__main__':
    # scr = Image.open(r"E:\python\untitled\加减大师作弊\venv\Images\1.png")
    # Init()
    '''HorCut(binarize(scr))'''
    a = binarize(Image.open(r"E:\python\untitled\加减大师作弊\venv\Images\56.png"), threshold=90)  # 测试所用

   #ImgHashRecognit(a)
    '''img = Image.open(path)  # 打开一张图片
    img = img.convert('L')  # 灰度转化
    re_img = img.point(table, mode)  # 在将灰度图像转换为位图图像（模式”1“）时，所有非零值都设置为255（白色）
    newimg = img.crop(left, up, right, bottom)  # 裁剪
    small_img = re_img.resize((width, height), mode)  # 缩小图片这里用 mode=Image.LANCZOS
'''
    # ResultByOcr(Image.open(r"E:\python\untitled\加减大师作弊\venv\Images\12.png"))
