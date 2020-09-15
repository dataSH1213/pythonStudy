### 2. 다음과 같은 계산기 코드가 있을 때, 상세하게 살을 덧붙이고,
###    예외처리와 모듈화를 진행하라.
def Cal() :
        try :
            num1 = int(input("숫자 입력 : ")) # 숫자1 입력부
            oper = input("연산자 입력 : ")    # 연산자 입력부
            num2 = int(input("숫자 입력 : ")) # 숫자2 입력부
            if oper == "+" :
                result = num1 + num2
                print(num1, "+", num2, "=", result)
            elif oper == "-" :
                result = num1 - num2
                print(num1, "-", num2, "=", result)
            elif oper == "*" :
                result = num1 * num2
                print(num1, "*", num2, "=", result)
            elif oper == "/" :
                result = num1 / num2
                print(num1, "/", num2, "=", result)
            elif oper == "%" :
                result = num1 % num2
                print(num1, "%", num2, "=", result)
            else :
                print("숫자와 연산자를 확인해주세요.")
        except ZeroDivisionError as e:
            print(e)
        except ValueError as f:
            print(f)

if __name__ == "__main__":
    Cal()

### 5. 영한사전 프로그램을 만들어라. 딕셔너리를 이용할 것
###    모듈화 / 예외처리 할 것

def dic() :
    words = {"apple":"사과", "banana":"바나나", "camel":"낙타"} # 딕셔너리 자료형
    select = input("1. 전체출력\n2. 영어로검색\n3. 한글로검색\n선택사항을 입력하세요 : ")
    # 전체출력
    if select == "전체출력" :
        for key,value in words.items() :
            print(key,":",value,sep = '')

    # 영어로검색
    elif select == "영어로검색" :
        eWords = input("검색어를 입력하세요 :")
        if(eWords == "apple") :
            print(words.get("apple"))
        elif(eWords == "banana") :
            print(words.get("banana"))
        elif(eWords == "camel") :
            print(words.get("camel"))
        else :
            print("검색어가 잘못되거나, 없는 단어입니다.")

    # 한글로검색
    elif select == "한글로검색" :
        kWords = input("검색어를 입력하세요 :")
        for key, value in words.items() :
            if value == kWords :
                print(key)
            else :
                print("검색어가 잘못되거나, 없는 단어입니다.")
    else :
        print("선택사항을 다시 입력해주세요.")

if __name__ == "__main__":
    dic()
