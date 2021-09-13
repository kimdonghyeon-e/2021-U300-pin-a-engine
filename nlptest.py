##포크하면 konlpy가 작동을 안함
import os
import time
# from konlpy.tag import Okt
# okt = Okt()

while(True) :
    time.sleep(0.5)
    processid = os.fork()

    if processid :
        from konlpy.tag import Okt
        okt = Okt()
        malist = okt.pos("당신을 사랑합니다.", norm=True, stem=True)
        print(malist)
        for printloop in range(len(malist)) :
            print(malist[printloop][0])
        # time.sleep(10)

    else :
        print("자식")
        # time.sleep(10)