import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중 중복 없이 6개를 임의로 추출
    numbers = random.sample(range(1, 46), 6)
    # 번호를 오름차순으로 정렬
    numbers.sort()
    return numbers

# 실행 및 결과 출력
if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("✨ 이번 주 추천 로또 번호 ✨")
    print(lotto_numbers) 

