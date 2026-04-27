import streamlit as st
import time

st.set_page_config(page_title="스타트업 창업 시뮬레이터", page_icon="🚀", layout="centered")

st.markdown("""
<style>
body {background-color: #f5f7fb;}
h1 {text-align: center; color: #222 !important; font-size: 40px;}
.stButton>button {
    background-color: #FF6B35;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stRadio > div {
    background-color: white;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 스타트업 창업 시뮬레이터")

col1, col2 = st.columns(2)
with col1:
    st.info("학번: 2025404052")
with col2:
    st.info("이름: 임정윤")

st.markdown("---")

@st.cache_data
def load_questions():
    time.sleep(2)
    return [
        ("Q1. 창업 아이템을 정할 때 가장 먼저 할 일은?", ["내가 만들고 싶은 서비스부터 정한다", "사람들이 실제로 불편해하는 문제를 찾는다"], "market"),
        ("Q2. 첫 서비스는 어떤 형태로 출시할까?", ["기능을 최대한 많이 넣고 출시한다", "핵심 기능만 담은 MVP로 빠르게 출시한다"], "market"),
        ("Q3. 사용자가 앱을 설치했는데 금방 삭제한다면?", ["디자인을 더 화려하게 바꾼다", "삭제 이유를 설문/인터뷰로 확인한다"], "market"),
        ("Q4. 팀원이 ‘이 기능 꼭 넣자’고 강하게 주장한다면?", ["일단 개발해서 넣어본다", "사용자에게 필요한 기능인지 먼저 검증한다"], "market"),
        ("Q5. 투자자 앞에서 가장 먼저 보여줄 자료는?", ["기술 구조도와 코드 완성도", "사용자 증가율과 시장 문제"], "market"),
        ("Q6. 경쟁사가 비슷한 서비스를 먼저 출시했다면?", ["기능을 더 많이 추가해서 따라잡는다", "우리가 더 잘 해결할 수 있는 틈새 문제를 찾는다"], "market"),
        ("Q7. 출시 후 악플이 달렸다면?", ["무시하고 계속 개발한다", "불만 속에서 개선 포인트를 찾는다"], "market"),
        ("Q8. 마케팅 예산이 거의 없다면?", ["광고비가 생길 때까지 기다린다", "커뮤니티, 숏폼, 지인 테스트로 반응을 본다"], "market"),
        ("Q9. 개발 일정이 계속 밀린다면?", ["완성도를 위해 계속 미룬다", "우선순위를 줄이고 핵심 기능부터 배포한다"], "market"),
        ("Q10. 서비스가 조금 성장했을 때 가장 위험한 선택은?", ["지표를 보고 다음 전략을 세운다", "갑자기 기능을 많이 늘리고 방향을 자주 바꾼다"], "risk"),
    ]

@st.cache_data
def load_results():
    return {
        "unicorn": {
            "title": "🦄 유니콘 기업 가능성",
            "desc": "시장 문제를 잘 파악하고, 빠르게 실험하며, 사용자 중심으로 성장할 수 있는 창업가 유형입니다.",
            "features": [
                "사용자 문제를 먼저 찾음",
                "MVP 출시와 피드백 반영이 빠름",
                "시장성과 성장 지표를 중요하게 봄"
            ],
            "advice": "사용자 인터뷰, MVP 테스트, 핵심 지표 분석을 반복하면 실제 창업 프로젝트로 발전시키기 좋습니다.",
            "color": "#8E44AD"
        },
        "stable": {
            "title": "📈 안정 성장형 스타트업",
            "desc": "위험을 줄이면서도 꾸준히 개선하고 성장할 가능성이 높은 창업가 유형입니다.",
            "features": [
                "현실적인 선택을 잘함",
                "사용자 반응을 어느 정도 반영함",
                "무리한 확장보다 안정적 운영을 선호함"
            ],
            "advice": "조금 더 빠른 실험과 적극적인 마케팅 테스트를 하면 성장 속도를 높일 수 있습니다.",
            "color": "#27AE60"
        },
        "funding": {
            "title": "💸 자금난 스타트업",
            "desc": "아이디어나 기술력은 있지만 시장 검증과 고객 확보 전략이 부족해 자금 압박을 받을 수 있는 유형입니다.",
            "features": [
                "기술 구현에 집중하는 경향",
                "고객 확보 전략이 약할 수 있음",
                "투자 설득에 필요한 데이터가 부족할 수 있음"
            ],
            "advice": "기능 개발보다 먼저 고객 문제, 시장 규모, 수익 모델을 검증하는 것이 중요합니다.",
            "color": "#F39C12"
        },
        "fail": {
            "title": "🔥 3개월 폐업 위험",
            "desc": "완성도나 아이디어에만 집중하다가 사용자와 시장 반응을 놓칠 가능성이 높은 유형입니다.",
            "features": [
                "출시가 늦어질 가능성이 큼",
                "사용자 피드백 반영이 부족함",
                "마케팅과 팀 운영 전략이 약할 수 있음"
            ],
            "advice": "처음부터 완벽한 서비스를 만들기보다 작게 출시하고 빠르게 수정하는 방식이 필요합니다.",
            "color": "#E74C3C"
        }
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.subheader("🔐 로그인")

user_id = st.text_input("아이디")
user_pw = st.text_input("비밀번호", type="password")

users = {
    "test": "1234",
    "admin": "admin123"
}

if st.button("로그인"):
    if user_id in users and users[user_id] == user_pw:
        st.session_state.logged_in = True
        st.success(f"{user_id}님 로그인 성공!")
    else:
        st.error("아이디 또는 비밀번호가 틀렸습니다.")

st.write("현재 상태:", "로그인됨" if st.session_state.logged_in else "로그인 안됨")

st.markdown("---")

if st.session_state.logged_in:
    st.subheader("💼 창업 의사결정 퀴즈")

    with st.spinner("창업 시뮬레이션 데이터를 불러오는 중입니다..."):
        questions = load_questions()

    st.caption("⚡ 퀴즈 데이터와 결과 데이터에는 Streamlit 캐싱이 적용되어 있습니다.")

    answers = []

    for i, (question, options, _) in enumerate(questions):
        answer = st.radio(question, options, index=None, key=i)
        answers.append(answer)

    answered_count = sum(1 for a in answers if a is not None)
    progress = answered_count / len(answers)

    st.progress(progress)
    st.write(f"📊 진행률: {answered_count} / {len(answers)}")

    success_score = 0
    risk_score = 0

    for i, (_, options, good_type) in enumerate(questions):
        if answers[i] is not None:
            if good_type == "market":
                if answers[i] == options[1]:
                    success_score += 1
                else:
                    risk_score += 1
            else:
                if answers[i] == options[0]:
                    success_score += 1
                else:
                    risk_score += 1

    result_data = load_results()

    st.markdown("---")

    if st.button("🚀 창업 결과 확인"):

        if None in answers:
            st.warning("모든 질문에 답해주세요!")
        else:
            total = success_score + risk_score
            success_percent = int((success_score / total) * 100)
            risk_percent = 100 - success_percent

            if success_percent >= 80:
                result = "unicorn"
            elif success_percent >= 60:
                result = "stable"
            elif success_percent >= 40:
                result = "funding"
            else:
                result = "fail"

            res = result_data[result]

            st.markdown(f"""
            <div style="padding:25px; border-radius:15px; background-color:{res['color']}; color:white;">
                <h2 style="text-align:center;">{res['title']}</h2>
                <p style="text-align:center;">{res['desc']}</p>
                <h3 style="text-align:center;">성공 가능성 {success_percent}% / 리스크 {risk_percent}%</h3>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🔍 주요 특징")
            for feature in res["features"]:
                st.write(f"✔ {feature}")

            st.markdown("### 💡 창업 조언")
            st.success(res["advice"])