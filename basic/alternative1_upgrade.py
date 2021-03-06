print("+, - 을 번갈아 출력합니다.")

n = int(input("몇 개를 출력할까?:"))

# +- 를 n // 2개의 출력
# 파이썬에서는 무시하고 싶은 값을 _(언더스코어) 로 사용할 수 있다.
# 여기선 순서말고는 아무런 의미가 없기 때문에 _ 를 사용했다.
# for _ in range(1, n // 2+1):  # 카운터용 변수가 1일 때
for _ in range(n // 2):     # 카운터용 변수가 0일 때
    print("+-", end="")

# n 이 홀수일 때만 + 를 출력(0이니까 false 라 아래 코드를 실행하지 않음)
if n % 2:
    print("+", end="")
print()
print("n % 2 출력값: ", n % 2)
