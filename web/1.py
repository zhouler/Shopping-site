from datetime import *
import os

def input1():
    try:
        h, m, s = (input("请设置关机时间！默认：23 00 00").split())
        print(h, m, s)

    except ValueError:
        print("格式输入错误,请重新输入")
        return input()
    else:
        print("关机时间设置ok")
        return 1
if __name__ == '__main__':
    # q=int(input())
    # input1()

    while 1:
        now_time = datetime.now()
        if int(now_time.hour)==0 and int(now_time.minute)==0 and int(now_time.second)==0:
            os.system('shutdown -s -f -t 59')
            break
