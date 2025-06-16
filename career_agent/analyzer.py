import json
from openai import OpenAI
from config import MODEL_NAME, OPENAI_API_KEY
from prompt_templates import analyze_prompt

def analyze_user(text):
    if not text.strip():
        return json.dumps({
            "personality": "입력 오류",
            "skills": "입력 오류",
            "error": "텍스트가 비어있습니다"
        }, ensure_ascii=False)

    try:
        # Initialize client with API key
        client = OpenAI(api_key=OPENAI_API_KEY)
        prompt = analyze_prompt.format(text=text)
        
        # Use new API format
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 진로 상담 전문가입니다. JSON 형식으로 응답해주세요."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        # Get and validate response
        result = response.choices[0].message.content
        json.loads(result)  # Validate JSON format
        return result  # Already JSON string, no need to dump again

    except Exception as e:
        return json.dumps({
            "personality": "분석 실패",
            "skills": "분석 실패",
            "error": str(e)
        }, ensure_ascii=False)