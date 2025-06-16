analyze_prompt = """
당신은 진로 상담 전문가입니다. 사용자의 텍스트를 기반으로 성향과 기술 수준을 분석해 주세요.

### 사용자 설명:
{text}

### 출력 예시 (JSON):
{{
  "personality": "문제 해결을 즐기고 분석적인 사고를 좋아함",
  "skills": ["Python", "데이터 분석"],
  "confidence_score": 0.9
}}
"""

recommend_prompt = """
당신은 진로 상담 전문가입니다. 아래 사용자 정보에 기반하여 적합한 직무와 산업을 추천해 주세요.

### 사용자 정보:
성향: {personality}
기술: {skills}

### 출력 예시 (JSON):
{{
  "recommended_roles": ["데이터 분석가", "AI 리서처"],
  "industries": ["핀테크", "헬스케어"],
  "advice": "Python과 SQL 기반의 실무 프로젝트 경험을 쌓으세요.",
  "confidence_score": 0.85
}}
"""