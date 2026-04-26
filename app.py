import streamlit as st


st.set_page_config(page_title="개발자 성향 테스트", page_icon="💻", layout="centered")


st.markdown("""
<style>
body {background-color: #f5f7fb;}
h1 {text-align: center; color: #4A90E2;}
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

    st.subheader(" 테스트 시작")

    
    q1 = st.radio("Q1. 더 끌리는 작업은?", ["UI 디자인", "서버 로직"], index=None)
    q2 = st.radio("Q2. 더 성취감을 느끼는 순간은?", ["UI 완성", "API 동작"], index=None)
    q3 = st.radio("Q3. 문제 해결 방식은?", ["눈에 보이는 결과 먼저", "내부 구조 먼저"], index=None)
    q4 = st.radio("Q4. 더 관심 있는 기술은?", ["프론트 기술", "백엔드 기술"], index=None)
    q5 = st.radio("Q5. 협업 시 더 편한 대상은?", ["디자이너", "서버 개발자"], index=None)
    q6 = st.radio("Q6. 더 중요하게 생각하는 것은?", ["사용자 경험", "성능"], index=None)
    q7 = st.radio("Q7. 더 흥미로운 작업은?", ["애니메이션", "데이터 처리"], index=None)
    q8 = st.radio("Q8. 디버깅 시 더 익숙한 것은?", ["UI 문제", "서버 문제"], index=None)
    q9 = st.radio("Q9. 더 스트레스 받는 상황은?", ["UI 깨짐", "서버 오류"], index=None)
    q10 = st.radio("Q10. 미래 목표는?", ["서비스 개발", "시스템 설계"], index=None)


    answers = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
    answered_count = sum([1 for a in answers if a is not None])
    progress = answered_count / len(answers)

    st.progress(progress)
    st.write(f"📊 진행률: {answered_count} / {len(answers)}")

  
    score_front = 0
    score_back = 0

    def calc(answer, front):
        return (1, 0) if answer == front else (0, 1)

    questions = [
        (q1, "UI 디자인"),
        (q2, "UI 완성"),
        (q3, "눈에 보이는 결과 먼저"),
        (q4, "프론트 기술"),
        (q5, "디자이너"),
        (q6, "사용자 경험"),
        (q7, "애니메이션"),
        (q8, "UI 문제"),
        (q9, "UI 깨짐"),
        (q10, "서비스 개발"),
    ]

    for q, f in questions:
        if q is not None:
            f_score, b_score = calc(q, f)
            score_front += f_score
            score_back += b_score

  
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

    if st.button(" 결과 확인"):

        if None in answers:
            st.warning("모든 질문에 답해주세요!")
        else:
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
            </div>
            """, unsafe_allow_html=True)

            
            st.markdown("### 🔍 주요 특징")
            for f in res["features"]:
                st.write(f"✔ {f}")

            st.markdown("### 🛠️ 추천 기술")
            st.info(res["tech"])

            st.markdown("### 💡 성장 방향")
            st.success(res["tip"])