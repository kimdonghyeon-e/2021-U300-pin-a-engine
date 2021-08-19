import os
import time
import pymysql
from konlpy.tag import Okt

##자연어처리 및 word2vec모델 임포트
okt = Okt()
import gensim
from gensim.models import word2vec
model = gensim.models.word2vec.Word2Vec.load('newwiki.model')
word_vectors = model.wv

##파이프라인 선언
r, w = os.pipe()

##이전 마지막 서치번호 저장된 것 가져오기
lastsearchfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'r')
lastsearch = lastsearchfile.readlines()
last = int(lastsearch[0])
# print("저번서치끝 ", last)

##무한루프, 서치테이블에 추가된 데이터 있는지 검사
while(True) :
    time.sleep(0.5)

    # print(last)

    ##DB에 연결 및 계속 쿼리 질의
    db = pymysql.Connect(host='localhost', user='root', password='ROOTuser1234', database='fdtest')
    cusor = db.cursor()
    query = "select * from search"
    cusor.execute(query)
    result = cusor.fetchall()

    print(result)

    size = len(result)
    # print("현재서치끝 ", size)

    ##만약 서치테이블에 추가된 데이터 있으면
    if size > last :

        ##해당 추가된 데이터만큼 포크
        for forkloop in range(size - last) :
            print("포크루프", forkloop)
            processid = os.fork()

            ##부모프로세스는 그냥 건너뛰기(계속 루프돌며 서치테이블 감시)
            if processid :
                # print("부모")
                forkloop

            ##자식프로세스에서 검색엔진 기능 진행
            else :
                # time.sleep(10)
                # print("자식")
                ##여기에 검색엔진 돌아갈 코드 입력하면 됨

                ##자식프로세스가 추가적인 자식프로세스 열지못하도록 종료
                exit()

        ##마지막서치번호 최신화
        wfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'w')
        wfile.write(str(result[size-1][0]))
        last = int(result[size-1][0])
        # print(str(result[size-1][0]))
        print(last)
    # break

            



# child_writes = "Hello geeks"

# processid = os.fork()
# if processid :
#     os.close(w)
#     r = os.fdopen(r)
#     print("parent reading")
#     str = r.read()
#     print("parent reads =", str)
# else :
#     os.close(r)
#     w = os.fdopen(w, 'w')
#     print("child writing")
#     w.write(child_writes)
#     print("child writes =", child_writes)
#     w.close()

# child_writes = "Hello geeks"