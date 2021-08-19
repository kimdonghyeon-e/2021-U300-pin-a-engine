import os
import subprocess
import json
import time
import pymysql

class SubprocessTest :
    def __init__(self) :
        program = r"/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/child.py"
        pro = subprocess.Popen(["python", program], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # stdout, stderr = pro.communicate()
        print("child run success!")

        db = pymysql.Connect(host='localhost', user='root', password='ROOTuser1234', database='fdtest')
        cusor = db.cursor()

        lastsearchfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'r')
        lastsearch = lastsearchfile.readlines()
        last = int(lastsearch[0])
        print(last)

        while(True) :
            query = "select * from search"
            cusor.execute(query)
            result = cusor.fetchall()

            print(result)

            size = len(result)

            if size > last : 
                # for searchloop in range(size - last) :
                #     data = result[last+searchloop+1][0].encode()
                #     pro.stdin.write(data)
                #     time.sleep(0.1)
                #     stdout, stderr = pro.communicate()
                #     print(stdout.decode('utf-8'))

                data = str(result[last][0]).encode()
                pro.stdin.write(data)
                time.sleep(0.1)
                stdout, stderr = pro.communicate()
                print(stdout.decode('utf-8'))

                wfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'w')
                wfile.write(str(result[last][0]))
                last = int(result[last][0])

            time.sleep(0.5)
            

if __name__ == "__main__" :
    SH = SubprocessTest()