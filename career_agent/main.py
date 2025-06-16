import json
from analyzer import analyze_user
from recommender import recommend_career

def main():
    print("🎯 진로 상담 에이전트에 오신 걸 환영합니다!")
    user_input = input("당신의 관심사, 잘하는 기술, 하고 싶은 일을 자유롭게 입력하세요:\n\n> ")

    print("\n📊 분석 중...")
    analysis_raw = analyze_user(user_input)
    print(f"\n[성향 분석 결과]\n{analysis_raw}")

    try:
        analysis = json.loads(analysis_raw)
    except json.JSONDecodeError:
        print("❌ 분석 결과를 파싱할 수 없습니다.")
        return

    print("\n🔍 진로 추천 중...")
    recommendation_raw = recommend_career(analysis['personality'], analysis['skills'])
    print(f"\n[추천 결과]\n{recommendation_raw}")

if __name__ == "__main__":
    main()