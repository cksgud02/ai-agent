import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다")

# OpenAI 설정
import openai
openai.api_key = OPENAI_API_KEY

MODEL_NAME = "gpt-3.5-turbo"