# app/core/llm_config.py

# langchain-ollama 패키지에서 ChatOllama를 임포트
from langchain_ollama import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel

from app.core.settings import settings 


def get_ollama_chat_model() -> BaseChatModel:
    """
    설정을 기반으로 ChatOllama 모델 객체를 반환합니다.
    """
    return ChatOllama(
        model=settings.OLLAMA_MODEL, 
        base_url=settings.OLLAMA_BASE_URL,
        temperature=0.0,
    )