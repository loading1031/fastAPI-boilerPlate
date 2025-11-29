# app/api/routes.py (신규 파일)

from fastapi import APIRouter
# 개별 Controller 파일에서 정의한 라우터를 임포트합니다.
from app.api import weather 

# 모든 라우터를 포함할 최상위 라우터 인스턴스를 생성합니다.
api_router = APIRouter()

# weather 라우터를 포함시킵니다.
# prefix="/weather"는 weather.py 내부가 아닌, 여기서 설정해야 최상위 URL 관리가 쉽습니다.
api_router.include_router(
    weather.weather_router, 
    tags=["Weather Agent"], 
    prefix="/weather"
)