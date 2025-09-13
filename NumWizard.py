# 간단 계산기 프로그램
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다!"
    return a / b

def calculator():
    while True:
        print("\n=== 간단 계산기 ===")
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 종료")
        
        choice = input("원하는 기능 번호를 입력하세요 (1-5): ")

        if choice == "5":
            print("계산기를 종료합니다. 안녕!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                num2 = float(input("두 번째 숫자를 입력하세요: "))
            except ValueError:
                print("숫자를 올바르게 입력해주세요!")
                continue

            if choice == "1":
                print(f"결과: {add(num1, num2)}")
            elif choice == "2":
                print(f"결과: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"결과: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"결과: {divide(num1, num2)}")
        else:
            print("잘못된 입력입니다. 1~5 사이 숫자를 입력해주세요.")

calculator()
