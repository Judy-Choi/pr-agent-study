# module_b.py

from module_a import greet, Calculator

def main():
    print(greet("Judy"))

    calc = Calculator()
    # module_a 에 없는 함수 참조 (calc.add(1,2) 를 사용해야 함!)
    result = calc.min(1, 2)
    print("1 + 2 =", result)

if __name__ == "__main__":
    main()
