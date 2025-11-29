# app/core/tools.py
import random
from langchain.tools import tool


@tool
def get_current_weather(city: str) -> str:
    """
    현재 도시의 날씨 정보를 상세하게 조회합니다.
    입력(city): 날씨를 알고 싶은 도시 이름 (예: "서울", "뉴욕")
    """
    # NOTE: 실제 API 호출 로직 대신 더미 데이터를 반환합니다.
    if "Seoul" in city:
        temp = random.randint(15, 25)
        return f"현재 서울의 날씨는 맑고 화창하며, 기온은 {temp}도입니다. 바람은 거의 불지 않습니다."
    elif "NewYork" in city:
        return "현재 뉴욕은 흐리고 비가 내리며, 기온은 10도입니다."
    else:
        return f"죄송합니다. {city}의 날씨 정보는 찾을 수 없습니다."