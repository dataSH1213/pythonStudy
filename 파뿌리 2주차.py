# 파뿌리 2주차 과제
# 민수홍
# 2020.09.14

### 1. 로또 번호 생성기 함수 만들기. 정렬까지 포함할 것
import random
def lotto() :
    lottoNum = random.sample(range(1,46),6) # 1~45 범위에서 6개 복원추출
    print(sorted(lottoNum))


### 2. 다음과 같은 계산기 코드가 있을 때, 상세하게 살을 덧붙이고,
###    예외처리와 모듈화를 진행하라.
import myMod1
myMod1.Cal()


### 3. 문자열을 분석하는 함수 만들기. 내장함수를 이용하라
def strAnl() :
    munja = str(input("문자열을 입력하세요 : "))
    print("문자의 개수 : %d" % len(munja))
    print("가장 큰 문자열 :",max(munja))
    print("뒤집은 문자열 :",munja[::-1])


### 4. 내장함수와 datetime라이브러리를 이용하여, 지금을 출력하고,
###    49일 1시간 8분 7초 후가 언제인지 출력하는 함수를 만드시오.
import datetime
def dTime() :
    # 현재시각 출력
    now = datetime.datetime.today() #현재시각 출력
    nTime = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초") #시각 나타내는 폼 변경
    print("현재 :",nTime)
    # 현재시각 + (49일 1시간 8분 7초)
    future = now + datetime.timedelta(days = 49,
                                      hours = 1,
                                      minutes = 8,
                                      seconds = 7)      
    fTime = future.strftime("%Y년 %m월 %d일 %H시 %M분 %S초") #시각 나타내는 폼 변경
    print("미래 :", fTime)
if __name__ == "__main__":
    dTime()

### 5. 영한사전 프로그램을 만들어라. 딕셔너리를 이용할 것
###    모듈화 / 예외처리 할 것
import myMod1
myMod1.dic()
