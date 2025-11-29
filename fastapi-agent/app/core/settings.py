# app/core/settings.py

import os
# from dotenv import load_dotenv # 💡 삭제: 이제 Docker가 로드합니다.

# 환경 변수 정의 및 기본값 설정
class Settings:
    """Docker Compose가 주입한 환경 변수를 os.getenv()로 읽습니다."""
    
    # 💡 Docker Compose에서 주입받은 OLLAMA_BASE_URL을 사용
    # 기본값은 로컬 테스트용으로만 남겨둡니다.
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "qwen2.5")
    APP_ENV: str = os.getenv("APP_ENV", "development")

settings = Settings()