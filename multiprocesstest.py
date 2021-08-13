import os
import subprocess

class SubprocessTest :
    def __init(self) :
        program = "notepad.exe"
        pro = subprocess.Popen(program, dtdin = subprocess.PIPE, sterr = subprocess.PIPE, stdout = subprocess.PIPE)
        data = "This is data".encode()
        pro.communicate(input = data)

if __name__ == "__main__" :
    SH = SubprocessTest()