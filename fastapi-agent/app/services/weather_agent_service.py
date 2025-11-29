# app/services/weather_agent_service.py

import json
from typing import Any, Dict, Union
from langchain_core.messages import BaseMessage

from app.core.agent_config import WEATHER_AGENT_RUNNABLE 


def safe_serialize(obj):
    """JSON 직렬화가 안 되는 객체를 만나면 문자열로 변환"""
    try:
        return obj.dict() # Pydantic v1 모델인 경우
    except:
        return str(obj)   # 그 외(AIMessage 등)는 그냥 문자열로 변환

def run_weather_agent(query: str) -> str:
    try:
        print(f"🚀 Running Agent with query: {query}", flush=True)
        
        # 1. 바뀐 입력 방식 (messages 리스트)
        response: Dict[str, Any] = WEATHER_AGENT_RUNNABLE.invoke({
            "messages": [
                {"role": "user", "content": query}
            ]
        })
        
        # 2. 결과 꺼내는 로직[1]
        if "messages" in response:
            # 리스트의 맨 마지막 메시지가 AI의 답변입니다.
            last_message: Union[BaseMessage, Dict[str, Any]] = response["messages"][-1]
            
            # 객체일 수도 있고 딕셔너리일 수도 있어서 안전하게 처리
            if hasattr(last_message, "content"):
                # 멀티모달, 리스트로 응답받는 상황은 제외함(향후, 고도화)
                return str(last_message.content)
            elif isinstance(last_message, dict):
                return str(last_message.get("content", ""))
            else:
                return str(last_message)
                
        else:
            # 디버깅용 로그
            debug_log = json.dumps(response, default=safe_serialize, indent=2, ensure_ascii=False)
            return f"❌ 결과 형식을 알 수 없음. 전체 응답:\n{debug_log}"

    except Exception as e:
        print(f"🔥 AGENT ERROR: {e}", flush=True)
        return f"Agent 실행 중 에러 발생: {str(e)}"
    
'''
[1] response 구조 예시:
{
  "messages": [
    {
      "content": "what is your name?",
      "additional_kwargs": {},
      "response_metadata": {},
      "type": "human",
      "name": null,
      "id": "0a98edbf-bf8d-43a8-9cd1-ee70e82ab9f0"
    },
    {
      "content": "I am Qwen, an AI language model developed by Alibaba Cloud. How can I assist you today?",
      "additional_kwargs": {},
      "response_metadata": {
        "model": "qwen2.5-coder:7b",
        "created_at": "2025-11-29T14:59:25.036608342Z",
        "done": true,
        "done_reason": "stop",
        "total_duration": 3704486502,
        "load_duration": 1217457084,
        "prompt_eval_count": 34,
        "prompt_eval_duration": 789709917,
        "eval_count": 22,
        "eval_duration": 1683635336,
        "logprobs": null,
        "model_name": "qwen2.5-coder:7b",
        "model_provider": "ollama"
      },
      "type": "ai",
      "name": null,
      "id": "lc_run--10b6db0e-a345-4ac6-9709-b20e0af96d57-0",
      "tool_calls": [],
      "invalid_tool_calls": [],
      "usage_metadata": {
        "input_tokens": 34,
        "output_tokens": 22,
        "total_tokens": 56
      }
    }
  ]
}
'''