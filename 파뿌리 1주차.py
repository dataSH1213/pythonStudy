### 파뿌리 1주차 과제
### 2020.09.05 민수홍

### 1.변수 (숫자, 문자, 리스트)
# 1
국어 = 50
수학 = 80
영어 = 30
평균 = (국어 + 수학 + 영어) / 3
print("평균은",평균)

## 2
num = 409298570
#num을 2로 나눈 나머지가 1 == 홀수 / 0 == 짝수
if num % 2 == 1 :
    print(num,"은 홀수")
else :
    print(num, "은 짝수")

## 3
r = "국어:수학:영어:프로그래밍"
# : 를 , 로 대체
r = r.replace(":", ",")
print(r)

## 4
num4 = [1,70,3,80,5]
#list의 순서를 반대로 하는 내장함수
num4.reverse() 
print(num4)

## 5
list1 = ["파이썬은", "정말", "편하다"]
list2 = list1[0] + " " + list1[1] + " " + list1[2]
print(list2)
print(list1[0], list1[1], list1[2])


## 6
num6 = [1, 50, 410, 10, 3, 4, 5]
# list를 순서대로 정렬하는 함수 x.sort
num6.sort()
print(num6)

# 7
love = " i love you "
# 양쪽 공백을 없애는 함수 x.strip
love = love.strip()
print(love)


### 2. 제어문
## 1
add = 0
for i in range(1,101) :
    add = add + i
print("1~100까지 합은",add)

## 2
# num/result 초기값 0 설정
num = 0
result = 0 
while num < 100 :
    # num을 반복마다 + 1하기 위한 조건
    num = num + 1
    # 1 ~ 100 더하기
    result = result + num
    if num == 100 :
    # 출력 (num = 100)
        print("1~100까지 합은", result)
        

## 3
result = 0
for i in range(1,101) :
    if i % 3 == 0 :
        result = result + i
print(result)
## 4
classA = (70, 60, 55, 75, 95, 90, 80, 80, 85, 100)
aa = 0
for i in classA :       # classA 만큼 반복
    aa = aa + i
result = aa / len(classA)
print("A학급의 중간고사 평균은",result,"점")

## 5
list1 = [1, 3, 5, 40, 90, 100, 2020]

num = 0
for i in list1 :
    if i % 2 == 1 :
        list1[num] = list1[num] * 2
    num = num + 1       # 반복문이 반복되면 num + 1
print(list1)


## 6
for i in range(1,6) :
    print(i * "*")      # i 번만큼 * 입력후 출력 / print 시 줄바꿈



### 3. 함수와 입출력

## 1 학점 산출 함수
def grade(score) :
    if score <= 29 :                #%d = 정수(intger) 포맷 코드                
        print("score = %d"% score)  # score <= 29 == grade = F
        print("grade = F")              
    elif score <= 49 :
        print("score = %d"% score)  # score <= 49 == grade = F
        print("grade = C")
    elif score <= 79 :
        print("score = %d"% score)  # score <= 79 == grade = F
        print("grade = B")
    elif score <= 100 :
        print("score = %d"% score)  # score <= 100 == grade = F
        print("grade = A")
grade(99)        

## 2 짝수판별 프로그램
def even(number) :
    if number % 2 == 0 :            # number % 2 == 0 이면 짝수로 판별
        return(True)
    else :                          
        return(False)

number = int(input("짝수 판별할 숫자를 입력하세요 : "))
result = even(number)
print(result)


## 3 주민등록번호
number = input("주민등록번호를 입력하세요 : ")
def resi(number) :
    year = number[0:2]              # 입력값의 앞 두자리를 year에 할당
    print("출생년도 : %s년" % year) # year를 출생년도로 출력
    if number[7] == "1" :           # 1 / 2 = 남성 / 여성
        print("성별 : 남성")
    elif number[7] == "2" :
        print("성별 : 여성")
resi(number)


## 4 간단한 계산기 함수
def com(num1,comp,num2) :   #num1,2 = 숫자 comp = 연산기호
    if comp == "+" :        
        print("%s + %s = " % (num1,num2), int(num1) + int(num2))
    elif comp == "-" :
        print("%s - %s = " % (num1,num2), int(num1) - int(num2))
    elif comp == "*" :
        print("%s * %s = " % (num1,num2), int(num1) * int(num2))
    elif comp == "/" :
        print("%s / %s = " % (num1,num2), int(num1) / int(num2))
    elif comp == "%" :
        print("%s %% %s = " % (num1,num2), int(num1) % int(num2))
    elif comp == "//" :
        print("%s // %s = " % (num1,num2), int(num1) // int(num2))    

com(19,"//",2)


## 5 거스름돈 함수
def change(money) :
    coin = [5000, 1000, 500, 100, 50, 10] # 잔돈 list
    num = 0
    for i in coin :
        result = money // i
        money = money - (int(coin[num]) * result)
        print("%s원 :" % coin[num],"%d개" %result)
        num = num + 1

change(6890)

## 6 이차방정식의 근을 구하는 함
import math 
def gengong(sik) :
    x2location = sik.find("x")
    x1location = sik.rfind("x")
    # x^2, x 앞까지 슬라이싱 => 계수를 알기 위해
    a = int(sik[0:x2location])              # x^2 계수
    b = int(sik[x2location+3:x1location])   # x 계수
    c = int(sik[x1location+1:len(sik)])     # 1 계수
    result1 = (-b + math.sqrt(b ** 2 - (4 * a * c))) / 2 * a
    result2 = (-b - math.sqrt(b ** 2 - (4 * a * c))) / 2 * a
    print("input : %s" % sik)
    print("output : x1 = %s, x2 = %s" % (result1, result2))


gengong("1x^2+6x-27")


        
