# while문
# 조건이 False가 될때까지 반복

i = 1 # 초기식
while i <= 10: # 조건식
    print(f'{i}번째 자동화 작업 중')
    i = i + 1 # 증감식

# 무한 반복문
while True:
    X = input("종료하려면 exit를 입력하세요 >>>")
    if X == "exit":
        break