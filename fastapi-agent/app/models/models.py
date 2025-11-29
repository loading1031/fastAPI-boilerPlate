# 1. Pydantic Request DTO 정의: 요청 본문(Request Body) 구조 정의
from pydantic import BaseModel, Field


class AgentQueryRequest(BaseModel):
    # 클라이언트가 보낼 필드 이름은 'query'이고, 타입은 str입니다.
    # Field(..., description=...)를 통해 필드가 필수(Required)임을 명시하고 문서화를 추가합니다.
    query: str = Field(..., description="Agent에게 전달할 질문 텍스트")