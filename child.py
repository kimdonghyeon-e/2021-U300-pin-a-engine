import os
import subprocess
import time

class ChildProcess :
    def __init__(self) :
        cycle = 0
        while (True) :
            # data = input()
            # print(data)
            # if data!=NULL :
                # print(data)
            #     print('child')
            print(cycle)
            time.sleep(0.5)
            cycle = cycle + 1
            if cycle == 10 :
                break

if __name__ == "__main__" :
    SH = ChildProcess()