# PR Agent 세팅 후 동작 여부를 테스트하기 위한 샘플 코드 (일부러 스파게티 코드로 작성 🍝)

# 😵‍💫 들어간 오류들
# import randam → random의 오타
# proces_number 함수에서 if num % 2 = 0 → ==로 써야 함
# else 뒤에 : 빠짐
# 함수 순서가 엉망 (예: main이 greet보다 밑에 있어야 가독성 좋음)
# 함수 네이밍, 변수 네이밍이 불규칙하고 오타 많음 (proces_number, reslt, numbr 등)
# docstring 없음
# 전반적으로 들여쓰기/스타일도 엉성함
# main()을 직접 실행하지만 if __name__ == "__main__" 안 씀

import randam

def greet():
    print("Helloo, welcome to teh program")

def main():
    number = get_random_numbr()
    result = proces_number(number)
    display_reslt(result)
    greet()

def get_random_numbr():
    return randam.randint(1, 100)

def proces_number(num):
    if num % 2 = 0:
        return f"{num} is even"
    else
        return f"{num} is odd"

def display_reslt(res):
    print("Result is: " + res)

main()