# fastapi-agent/main.py
from fastapi import FastAPI
# 💡 routes.py에서 통합 라우터를 임포트합니다.
from app.api.routes import api_router 

# ----------------------------------------------------
# A. FastAPI 애플리케이션 인스턴스 생성
# ----------------------------------------------------
app = FastAPI(
    title="LLM FastAPI Agent",
    description="LangChain Agent Executor integrated with FastAPI and Ollama.",
    version="0.1.0",
)

# ----------------------------------------------------
# B. 라우터 등록
# ----------------------------------------------------
# 💡 통합된 api_router만 등록하고, V1 prefix를 부여합니다.
app.include_router(api_router, prefix="/api/v1") 