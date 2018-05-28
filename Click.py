import win32api, win32gui, win32con
from PIL import ImageGrab
from image import Result
import random
import time


def ClickOne():
    '''i=1#初始化函数  将123..原型载入
    while True:
        img=ImageGrab.grab((10,400,450,700))
        img.save('E:/python/untitled/加减大师作弊/venv/Images/'+str(i)+".png", 'png')
        i+=1
        print("ok!")
        time.sleep(1)
    '''
    try:
        img = ImageGrab.grab((10, 400, 450, 700))
        img.save(r"E:\python\untitled\加减大师作弊\venv\Images\55.png")
        if Result(img):
            print("正确!")
            win32api.SetCursorPos((random.randint(30, 110), random.randint(651, 709)))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        else:
            print("错误!")
            win32api.SetCursorPos((random.randint(220, 290), random.randint(650, 709)))  # 移动
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    except:
        time.sleep(100)
        win32api.SetCursorPos((random.randint(20, 150), random.randint(641, 779)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)#点击


# 测试
if __name__ == '__main__':

    img = ImageGrab.grab((10, 400, 450, 700)).show()
    while True:
        print(win32gui.GetCursorPos())
        time.sleep(2)
