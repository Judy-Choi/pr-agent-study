import datetime
import random

user_id_counter = 0

class Item:
    """
    아이템을 나타내는 클래스입니다.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created_at = datetime.datetime.now()

    def display_info(self):
        """아이템 정보를 출력합니다."""
        print(f"Item: {self.name}, Price: {self.price}, Created: {self.created_at}")

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"{self.name}의 가격이 {self.price}로 변경되었습니다.")
        else:
            print("유효하지 않은 가격입니다.")

# FIXME: 아래 함수는 현재 테스트 데이터에 의존하고 있음. 실제 데이터 소스 연결 필요.
def generate_sample_report(item_count=5):
    """
    샘플 보고서를 생성합니다.
    """
    print("--- 샘플 보고서 ---")
    items = []
    for i in range(item_count):
        # todo: 아이템 이름 생성 로직 다양화
        item_name = f"샘플 아이템 {i+1}"
        # Todo: 아이템 가격 범위를 좀 더 현실적으로 조정
        item_price = random.randint(1000, 50000)
        items.append(Item(item_name, item_price))

    for item in items:
        item.display_info()

def main():
    """
    메인 실행 함수입니다.
    """
    print("애플리케이션 시작...")

    item1 = Item("노트북", 1200000)
    item1.display_info()
    item1.update_price(1150000)

    generate_sample_report(3)

    print("애플리케이션 종료.")

if __name__ == "__main__":
    main()