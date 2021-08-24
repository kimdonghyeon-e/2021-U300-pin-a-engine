# 2021-U300-pin-a-engine

### 2021 U300 창업동아리 : 플라워드 엔진 개발


코드 소개 : 

    flowerengine.ipynb = 검색어와 꽃 사이의 유사도 높은 순 정렬

    mysqlsearch.ipynb = mysql연결 및 상품리스트의 키워드(가격, 꽃, 색 등)와 검색어 직접 비교해 가장 유사한 상품 순 정렬.

    mysqlorderprice.ipynb = mysql연결 및 이용자 구매내역 뽑아서 가격 가중평균 구하기.

    mysqlflowersearch.ipynb = mysql연결 및 상품리스트중 flowerengine결과와 일치하는 꽃 뽑기.

    nearprice.ipynb = 가중평균 +-10% 사이 가격 상품 뽑기.

    fork.py = 멀티프로세스 코드
              mysqlorderprice제외 모든 코드 통합 거의 완료.
              가격관련기능은 백엔드와 데베 맞춰야함.
              그 외 검색결과 백엔드에 줄 방법 고안 필요.


앞으로 해야할 일 :

    엘라스틱서치 공부

    백엔드 데베에 맞게 수정(mysqlorderprice.ipynb 아직 안함)(백엔드 데베바뀔때마다 배열 확인하기)

    코드 통합(fork.py에 통합중)

    기타등등...
    

참고 페이지 : 

    https://www.inflearn.com/course/elk-%EC%8A%A4%ED%83%9D-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D/#curriculum
    (엘라스틱서치)
