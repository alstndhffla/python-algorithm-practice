"""
거스름돈
당신은 음식점의 계산을 도와주는 점원. 카운터에 거스름돈 500원, 100원, 50원, 10원짜리 동전히 무한히 존재
손님에게 거슬러 줘야 할 돈이 N원 일 때 거슬러 줘야할 동전의 최소개수를 구하라.
단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.
"""

n = int(input("거슬러 받을 금액을 입력 : "))
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    # count += n//coin
    count = count + n//coin
    # 나누기 연산 후 몫이 아닌 나머지를 구해 n 에 대입
    # n %= coin
    n = n % coin

print(count)