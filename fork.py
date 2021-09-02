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

##꽃 리스트 추가
flower = ['갈대',
          '강아지풀', '개나리', '개망초', 
          '개양귀비', '갯버들',
          '공작초', '과꽃',
          '국화', '군자란', 
          '극락조화', '글록시니아', 
          '금낭화', '금목서', '금어초', '금잔화', '금작화', '기린초', '기생꽃', 
          '꽃잔디', '꽃창포', '꽈리', 
          '나팔꽃', '난초', '남천', '냉이', '넌출월귤', 
          '노루귀', 
          '능소화', '달리아', '달맞이꽃', 
          '담배',  
          '데이지', '도꼬마리', '도라지꽃', 
          '동백꽃', '독말풀', '둥글레', '들국화',
          '다알리아', 
          '라벤더', '라임', '라일락', '레몬',  
          '로즈마리', '로즈힙', 
          '루드베키아', '마가렛', '마로니에', 
          '마타리', '마시멜로', '만수국', '망초', '맨드라미', 
          '머위', '모란', '목련', '목향', '목화', '몬스테라', 
          '무궁화', '문주란', '물망초', '미나리', 
          '미나리아재비', '미모사', '민들레', '민트', 
          '바이올렛', '제비꽃', 
          '밤안개', '방울꽃', '배꽃', '백목련', '백일홍', '백합', 
          '벌개미취', '벚꽃', '베고니아', '보리', 
          '보리수', '봄맞이꽃', '봉선화', '부용', '부추', '분꽃', '붓꽃', 
          '빈카', '반다', '사루비아', 
          '사프란', '산나리', '산당화', '산딸기',
          '산세베리아', '산수유', '상사화', 
          '석류', '석산', '피안화', '꽃무릇', '선인장', 
          '세이지', '소철', '송엽국', 
          '수국', '수련', '수레국화', '센트레아', '수선화', '스노드롭', '스위트피',  
          '스타티스', 
          '아네모네',
          '아마', '아마릴리스', '아스타', '아스파라거스', 
          '아카시아', '안개꽃', 
          '앵초', '연근', '연꽃', '에델바이스', 
          '어성초', '억새', '엉겅퀴', 
          '양귀비', '양치', '영산홍', '오레가노', '오렌지', '오이풀', '옥수수', 
          '용담', '우엉', '유채꽃', '유칼립투스',  
          '으름덩굴', '은매화', '은방울꽃',
          '인디고', '일일초', '홍화', 
          '장미', '자스민', '제비꽃', '접시꽃', '제라늄', '진달래', 
          '자양화', '찔레꽃', 
          '작약', '창포', '채송화', '천일홍', 
          '철쭉', '칸나', '칼라', 
          '코스모스', '크로커스', '크랜베리', '카네이션', '코키아', '코리앤더', 
          '카사블랑카', '투구꽃', '튤립',
          '패랭이꽃', '팬지', '팽나무', '페퍼민트', 
          '프리지아', 
          '플라타너스', '해바라기', 
          '헬리오트롭', '헬리오트로프', '현호색', '협죽도', 
          '홉',  
          '히비스커스']

##꽃마다 유사도 메기기 위한 리스트. [][0]에는 유사도, [][1]에는 꽃이름
flowerscore = [[0]*2 for i in range(len(flower))]
for flowerlist in range(len(flower)) :
    flowerscore[flowerlist][1] = flower[flowerlist]

##파이프라인 선언
r, w = os.pipe()

##이전 마지막 서치번호 저장된 것 가져오기
lastsearchfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'r')
lastsearch = lastsearchfile.readlines()
last = int(lastsearch[0])
print("저번서치끝 ", last)

##DB연결
db = pymysql.Connect(host='localhost', user='root', password='ROOTuser1234', database='fdtest')
cusor = db.cursor()

##무한루프, 서치테이블에 추가된 데이터 있는지 검사
while(True) :
    time.sleep(0.5)

    # print(last)

    ##DB에 계속 쿼리 질의
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

                ##mysql로 입력받은 검색어 저장 및 형태소분리
                print(result[last+forkloop][2])
                searchword = result[last+forkloop][2]
                print("검색어 : ", searchword)
                malist = okt.pos(searchword, norm=True, stem=True)
                print("분리된 형태소 : ", malist)

                ##형태소 일부 전처리 및 '*색'키워드 분리(이부분에서 오류있음)
                colorlist = list(range(0))
                searchkeyword = list(range(0))
                for listloop in range(len(malist)) :
                    if "색" in malist[listloop][0] :
                        colorlist.insert(listloop, malist[listloop][0])
                    if not malist[listloop][1] in ["Josa", "Eomi", "Punctuation", "Alpha", "KoreanParticle"]:
                        flname = malist[listloop][0]
                        searchkeyword.insert(listloop, flname) 
                print("색 키워드 : ", colorlist)
                print("전처리된 검색어들 : ", searchkeyword)

                ##유사도 리스트에 입력
                nearkeyword = model.wv.most_similar(positive=searchkeyword, negative=[])
                for i in range(0, len(flower), 1) :
                    flowerscore[i][0] = word_vectors.similarity(w1=nearkeyword[0][0], w2=flower[i])

                ##유사도 내림차순 정렬
                sortflower = sorted(flowerscore, key = lambda x : -x[0])
                print("꽃 유사도 : ", sortflower)

                ##mysql접속해서 상품테이블 리스트 받아오기(presult)
                pdb = pymysql.Connect(hst='localhost', user='root', password='ROOTuser1234', database='fdtest')
                pcusor = pdb.connect
                pquery = "select * from price"
                pcusor.execute(pquery)
                presult = pcusor.fetchall()

                ##데이터마다 점수 메기기 위한 리스트. [][0]에는 점수, [][1]에는 상품번호
                tablescore = [[0]*2 for i in range(len(presult))]
                for makelist in range(len(presult)) :
                    tablescore[makelist][1] = presult[makelist][0]

                ##mysql검색루프(유사도검색 꽃 순위별 5~1점 제공, 단순비교검색 각각 1점 제공, 가격유사시 1점 제공(아직 데베 어떻게될지몰라서 이건 구현안함))
                for tableloop in range(len(presult)) :
                    for flowerfind in range(5) :
                        if sortflower[flowerfind][1] == presult[tableloop][9] :
                            if flowerfind == 0 :
                                tablescore[tableloop][0] += 5
                            elif flowerfind == 1 :
                                tablescore[tableloop][0] += 4
                            elif flowerfind == 2 :
                                tablescore[tableloop][0] += 3
                            elif flowerfind == 3 :
                                tablescore[tableloop][0] += 2
                            else :
                                tablescore[tableloop][0] += 1
                    for keywordloop in range(len(searchkeyword)) :
                        for searchloop in range(len(presult[0])) :
                            if searchkeyword[keywordloop] == result[tableloop][searchloop] :
                                tablescore[tableloop][0] += 1

                ##검색루프 돌아서 점수만든거 내림차순정렬
                sorttable = sorted(tablescore, key = lambda x : -x[0])
                print(sorttable)

                ##이제 이거를 어떻게 백엔드에주지,,?

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