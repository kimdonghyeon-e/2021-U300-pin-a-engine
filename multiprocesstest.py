import os
import subprocess
import json
import time

class SubprocessTest :
    def __init__(self) :
        program = r"/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/multiprocesschild.py"
        pro = subprocess.Popen(["python", program], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        data = "Hi there!".encode()  #그럼 이 데이터는 넘겨지지 않는가?
        pro.stdin.write(data)
        time.sleep(0.1)
        stdout, stderr = pro.communicate()
        print(stdout)
        print("------")
        print(stderr)
        print(stdout.decode('utf-8'))

if __name__ == "__main__" :
    SH = SubprocessTest()