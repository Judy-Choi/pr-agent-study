# TODO: 최상위 레벨 - 전체 애플리케이션 설정 로드 방식 개선 필요

import datetime

# todo: 이 모듈은 임시로 사용되며, 추후 더 안정적인 라이브러리로 대체해야 함
import random

# Todo: 전역 변수 사용을 최소화하고, 클래스나 함수 인자로 전달하는 방식 고려
user_id_counter = 0

class Item:
    """
    아이템을 나타내는 클래스입니다.
    """
    # TODO: 아이템 생성 시 고유 ID를 부여하는 더 나은 방법 모색 (예: UUID 사용)
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # todo: 가격 유효성 검사 추가 (0보다 커야 함)
        self.created_at = datetime.datetime.now()
        # Todo: 아이템 할인율 필드 추가 및 관련 로직 구현

    def display_info(self):
        """아이템 정보를 출력합니다."""
        # TODO: 출력 형식을 좀 더 사용자 친화적으로 변경
        print(f"Item: {self.name}, Price: {self.price}, Created: {self.created_at}")

    # todo: 아이템 가격 변경 시 로그를 남기는 기능 추가
    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"{self.name}의 가격이 {self.price}로 변경되었습니다.")
        else:
            # Todo: 잘못된 가격 입력 시 예외 처리 또는 경고 메시지 개선
            print("유효하지 않은 가격입니다.")

# FIXME: 아래 함수는 현재 테스트 데이터에 의존하고 있음. 실제 데이터 소스 연결 필요.
def generate_sample_report(item_count=5):
    """
    샘플 보고서를 생성합니다.
    """
    # TODO: 보고서 제목에 현재 날짜 포함시키기
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
    # TODO: 보고서 요약 정보(총 아이템 수, 평균 가격 등) 추가

def main():
    """
    메인 실행 함수입니다.
    """
    # Todo: 사용자 입력을 받아 아이템을 생성하는 기능 추가
    print("애플리케이션 시작...")

    # TODO: Item 클래스 인스턴스화 및 메소드 호출 예시
    item1 = Item("노트북", 1200000)
    item1.display_info()
    item1.update_price(1150000)

    # todo: generate_sample_report 함수 호출 시 인자 값 변경 테스트
    generate_sample_report(3)

    # Todo: 애플리케이션 종료 시 필요한 정리 작업 (예: 로그 파일 닫기)
    print("애플리케이션 종료.")

if __name__ == "__main__":
    # TODO: 명령줄 인자를 처리하여 프로그램 동작을 변경할 수 있도록 개선
    main()