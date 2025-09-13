import math
import os
import json # JSON 저장을 위해 추가

# 기본 연산 함수
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # 0으로 나누기 방지
    if b == 0:
        return "오류! 0으로 나눌 수 없습니다."
    return a / b

# 고급 연산 함수
def exponent(a, b):
    return a ** b

def square_root(a):
    # 음수에 대한 제곱근 계산 방지
    if a < 0:
        return "오류! 음수의 제곱근은 계산할 수 없습니다."
    return math.sqrt(a)

def modulus(a, b):
    # 0으로 나누기 방지
    if b == 0:
        return "오류! 0으로 나눈 나머지는 계산할 수 없습니다."
    return a % b

def absolute_value(a):
    return abs(a)

def factorial(a):
    # 음수 및 너무 큰 숫자에 대한 팩토리얼 계산 방지
    if a < 0:
        return "오류! 음수의 팩토리얼은 계산할 수 없습니다."
    if a > 100:
        return "오류! 팩토리얼 계산을 위한 입력이 너무 큽니다."
    return math.factorial(int(a))

# 추가 기능: 단위 변환 함수
def cm_to_m(cm):
    return cm / 100

def km_to_mile(km):
    return km * 0.621371

# 계산 기록을 파일에 저장하는 함수
def save_history(history):
    with open("calculator_history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
    print("계산 기록이 'calculator_history.json' 파일에 저장되었습니다.")

# 메인 계산기 함수
def calculator():
    history = []
    
    # ASCII 아트 로고
    print("------------------------------------------")
    print("""
 _____        _            _        _ _
/  __ \      | |          | |      | | |
| /  \/ __ _ | | __ _  ___| | __ _ | | |
| |    / _` || |/ _` |/ __| |/ _` || | |
| \__/| (_| || | (_| |\__ \ | (_| || | |
 \____/\__,_||_|\__,_||___/_|\__,_||_|_|
    """)
    print("✨ 고급 파이썬 CLI 계산기 ✨")
    print("------------------------------------------")

    while True:
        print("\n원하는 작업을 선택하세요:")
        print("1. 기본 연산 (+, -, *, /)")
        print("2. 고급 연산 (**, sqrt, %, abs, !)")
        print("3. 단위 변환 (cm→m, km→mile)")
        print("4. 기록 보기")
        print("5. 기록 저장")
        print("6. 종료")

        choice = input("선택 (1/2/3/4/5/6): ")

        if choice == '6':
            print("계산기를 종료합니다. 안녕히 가세요!")
            break

        elif choice == '4':
            if not history:
                print("기록이 비어 있습니다.")
            else:
                print("\n--- 계산 기록 ---")
                for item in history:
                    print(item)
                print("-------------------")
            continue

        elif choice == '5':
            if not history:
                print("저장할 기록이 없습니다.")
            else:
                save_history(history)
            continue
        
        try:
            if choice == '1':
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                operation = input("연산자 (+, -, *, /)를 입력하세요: ")
                num2 = float(input("두 번째 숫자를 입력하세요: "))

                result = ""
                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
                else:
                    result = "유효하지 않은 연산자입니다. 다시 시도해주세요."

                print(f"결과: {result}")
                history.append(f"{num1} {operation} {num2} = {result}")

            elif choice == '2':
                print("\n고급 연산:")
                print("  ^   - 제곱 (예: 2 ^ 3)")
                print("  sqrt - 제곱근 (예: sqrt 25)")
                print("  %    - 나머지 (예: 10 % 3)")
                print("  abs  - 절대값 (예: abs -5)")
                print("  !    - 팩토리얼 (예: 5!)")
                
                operation = input("연산을 입력하세요: ")
                
                result = ""
                if operation == '^':
                    num1 = float(input("밑(base)을 입력하세요: "))
                    num2 = float(input("지수(exponent)를 입력하세요: "))
                    result = exponent(num1, num2)
                    history.append(f"{num1} ^ {num2} = {result}")
                
                elif operation == 'sqrt':
                    num1 = float(input("숫자를 입력하세요: "))
                    result = square_root(num1)
                    history.append(f"sqrt({num1}) = {result}")
                    
                elif operation == '%':
                    num1 = float(input("피제수(나눠지는 수)를 입력하세요: "))
                    num2 = float(input("제수(나누는 수)를 입력하세요: "))
                    result = modulus(num1, num2)
                    history.append(f"{num1} % {num2} = {result}")
                
                elif operation == 'abs':
                    num1 = float(input("숫자를 입력하세요: "))
                    result = absolute_value(num1)
                    history.append(f"abs({num1}) = {result}")
                
                elif operation == '!':
                    num1 = int(input("숫자를 입력하세요: "))
                    result = factorial(num1)
                    history.append(f"{num1}! = {result}")

                else:
                    result = "유효하지 않은 연산입니다. 다시 시도해주세요."
                
                print(f"결과: {result}")

            elif choice == '3':
                print("\n단위 변환:")
                print("  1. cm → m")
                print("  2. km → mile")
                unit_choice = input("변환을 선택하세요 (1/2): ")
                
                if unit_choice == '1':
                    value = float(input("cm 값을 입력하세요: "))
                    converted_value = cm_to_m(value)
                    print(f"{value} cm는 {converted_value} m입니다.")
                    history.append(f"{value} cm = {converted_value} m")
                elif unit_choice == '2':
                    value = float(input("km 값을 입력하세요: "))
                    converted_value = km_to_mile(value)
                    print(f"{value} km는 {converted_value} mile입니다.")
                    history.append(f"{value} km = {converted_value} mile")
                else:
                    print("유효하지 않은 선택입니다. 다시 시도해주세요.")

            else:
                print("유효하지 않은 선택입니다. 1-6 사이의 유효한 옵션을 입력해주세요.")

        except ValueError:
            print("오류! 유효한 숫자를 입력해주세요.")
            
# 계산기 실행
if __name__ == "__main__":
    calculator()