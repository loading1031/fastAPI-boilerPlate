# app/core/agent_config.py (신규 파일)

from langchain.agents import create_agent
from langchain_core.runnables import Runnable
# 기존 LLM Config와 Tool 정의를 임포트
from app.core.errors import handle_tool_errors
from app.core.llm_config import get_ollama_chat_model
from app.core.tools import get_current_weather

# 1. 구성 요소 로드
chat_model = get_ollama_chat_model()

# 2. Chat Prompt Template 정의 (Configuration)
SYSTEM_PROMPT = """
You are a helpful assistant.
IMPORTANT: When you need to use a tool, do NOT output the JSON in the response content.
"""


# Agent는 Runnable 인터페이스를 따릅니다.
WEATHER_AGENT_RUNNABLE: Runnable = create_agent(
    model=chat_model, 
    # tools=[get_current_weather], 
    middleware=[handle_tool_errors],
    # system_prompt=SYSTEM_PROMPT
)