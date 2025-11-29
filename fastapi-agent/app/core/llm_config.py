# app/core/llm_config.py

from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

from app.core.settings import settings 


def get_chat_model() -> BaseChatModel:
    """
    설정을 기반으로 ChatOllama 모델 객체를 반환합니다.
    """
    return ChatOpenAI(
        model=settings.LLM_MODEL, 
        base_url=settings.LLM_URL,
        api_key='fake_api_key',  # Docker Model Runner는 API 키가 필요하지 않지만, langchain의 요구사항을 충족하기 위해 임의의 값을 사용합니다.
        temperature=0.0,
    )