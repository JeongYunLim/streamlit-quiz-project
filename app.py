import streamlit as st

st.set_page_config(page_title="개발자 성향 테스트", page_icon="💻", layout="centered")

st.markdown("""
<style>
body {background-color: #f5f7fb;}
h1 {text-align: center; color: #222 !important; font-size: 40px;}
.stButton>button {
    background-color: #4A90E2;
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

st.title("💻 개발자 성향 테스트")

col1, col2 = st.columns(2)
with col1:
    st.info("학번: 2025404052")
with col2:
    st.info("이름: 임정윤")

st.markdown("---")

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

    st.subheader("🚀 테스트 시작")

    questions = [
        ("Q1. 팀 프로젝트에서 더 스트레스 받는 상황은?", ["UI 깨짐", "서버 터짐"], "UI 깨짐"),
        ("Q2. 더 재밌다고 느끼는 작업은?", ["애니메이션 만들기", "API 설계"], "애니메이션 만들기"),
        ("Q3. 버그가 생겼을 때 먼저 보는 것은?", ["화면 출력", "로그/데이터 흐름"], "화면 출력"),
        ("Q4. 더 중요하게 생각하는 것은?", ["사용자 경험", "시스템 안정성"], "사용자 경험"),
        ("Q5. 더 하고 싶은 역할은?", ["디자인 구현", "데이터 처리"], "디자인 구현"),
        ("Q6. 프로젝트에서 더 뿌듯한 순간은?", ["UI 완성됐을 때", "서버 잘 돌아갈 때"], "UI 완성됐을 때"),
        ("Q7. 더 흥미로운 기술은?", ["React, CSS", "Database, API"], "React, CSS"),
        ("Q8. 디버깅할 때 더 편한 것은?", ["눈으로 보이는 문제", "코드 흐름 분석"], "눈으로 보이는 문제"),
        ("Q9. 더 자주 보는 것은?", ["브라우저 화면", "터미널 로그"], "브라우저 화면"),
        ("Q10. 미래에 더 하고 싶은 것은?", ["웹 서비스 만들기", "대규모 시스템 설계"], "웹 서비스 만들기"),
    ]

    answers = []

    for i, (q, options, _) in enumerate(questions):
        ans = st.radio(q, options, index=None, key=i)
        answers.append(ans)

    answered_count = sum([1 for a in answers if a is not None])
    progress = answered_count / len(answers)

    st.progress(progress)
    st.write(f"📊 진행률: {answered_count} / {len(answers)}")

    score_front = 0
    score_back = 0

    for i, (_, _, front_ans) in enumerate(questions):
        if answers[i] is not None:
            if answers[i] == front_ans:
                score_front += 1
            else:
                score_back += 1

    @st.cache_data
    def load_result():
        return {
            "frontend": {
                "title": "🎨 Frontend 개발자형",
                "desc": "사용자 경험(UI/UX)을 중요하게 생각하며 인터페이스 구현에 강점을 가진 개발자입니다.",
                "features": [
                    "디자인 감각이 뛰어남",
                    "사용자 중심 사고",
                    "인터랙션 구현 능력"
                ],
                "tech": "React, Vue, HTML, CSS, JavaScript",
                "tip": "👉 UI 클론 코딩과 애니메이션 구현을 많이 해보세요.",
                "color": "#4A90E2"
            },
            "backend": {
                "title": "🖥️ Backend 개발자형",
                "desc": "서버, 데이터 처리, 시스템 구조 설계에 강점을 가진 개발자입니다.",
                "features": [
                    "논리적 사고 능력",
                    "데이터 처리 능력",
                    "시스템 설계 이해도"
                ],
                "tech": "Spring, Node.js, Python, Database",
                "tip": "👉 API 설계와 DB 프로젝트 경험이 중요합니다.",
                "color": "#27AE60"
            },
            "fullstack": {
                "title": "🚀 Fullstack 개발자형",
                "desc": "프론트와 백을 모두 다룰 수 있는 균형형 개발자입니다.",
                "features": [
                    "전체 흐름 이해",
                    "기술 적응력",
                    "협업 능력"
                ],
                "tech": "Fullstack 프로젝트, DevOps",
                "tip": "👉 서비스 하나를 끝까지 만들어보세요.",
                "color": "#9B59B6"
            }
        }

    result_data = load_result()

    st.markdown("---")

    if st.button("📊 결과 확인"):

        if None in answers:
            st.warning("모든 질문에 답해주세요!")
        else:
            total = score_front + score_back
            front_percent = int((score_front / total) * 100)
            back_percent = 100 - front_percent

            if score_front > score_back:
                result = "frontend"
            elif score_back > score_front:
                result = "backend"
            else:
                result = "fullstack"

            res = result_data[result]

            st.markdown(f"""
            <div style="padding:25px; border-radius:15px; background-color:{res['color']}; color:white;">
                <h2 style="text-align:center;">{res['title']}</h2>
                <p style="text-align:center;">{res['desc']}</p>
                <h3 style="text-align:center;">Frontend {front_percent}% / Backend {back_percent}%</h3>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🔍 주요 특징")
            for f in res["features"]:
                st.write(f"✔ {f}")

            st.markdown("### 🛠️ 추천 기술")
            st.info(res["tech"])

            st.markdown("### 💡 성장 방향")
            st.success(res["tip"])