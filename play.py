from Click import ClickOne
import time
import random

if __name__ == '__main__':
    cnt=40

    while True:
        try:
            ClickOne()
        except:
            pass
        time.sleep(cnt*0.01)
        cnt=random.randint(29,49)
