# app/api/weather.py (수정)

from typing import Any, Dict
from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool

from app.models.models import AgentQueryRequest
from app.services.weather_agent_service import run_weather_agent

# B. FastAPI Router 정의
weather_router = APIRouter(
    tags=["Weather Agent"],
)


@weather_router.post("/query", response_model=Dict[str, Any])
async def process_agent_query(request: AgentQueryRequest):
    """
    엔드포인트는 이제 routes.py의 설정에 따라 /api/v1/weather/query 가 됩니다.
    """
    if not request.query:
        # 질문이 없는 경우 400 Bad Request 응답
        raise HTTPException(
            status_code=400, 
            detail="Query cannot be empty."
        )

    try:
        # 💡 핵심: 동기 함수인 run_weather_agent를 run_in_threadpool을 사용하여 호출하고 await 합니다.
        # 이렇게 하면 동기 작업이 별도의 스레드에서 실행되어 메인 비동기 루프를 블로킹하지 않습니다.
        result_text = await run_in_threadpool(run_weather_agent, request.query)
        
        # 클라이언트에게 최종 답변을 JSON 형태로 반환
        return {"query": request.query, "answer": result_text}

    except Exception as e:
        print(f"Agent processing error: {e}")
        # Agent 실행 중 내부 오류 발생 시 500 Internal Server Error 응답
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Agent Error: {e}"
        )