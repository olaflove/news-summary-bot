import streamlit as st
import feedparser
import os
from dotenv import load_dotenv
from openai import OpenAI

# [F01] 환경 변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- UI 설정 (코드 최상단에 배치하여 화면이 먼저 뜨게 함) ---
st.set_page_config(page_title="뉴스 요약 챗봇", page_icon="🤖")
st.title("🤖 AI 뉴스 아카이빙 챗봇")

# API 키 체크
if not api_key:
    st.error(".env 파일에 OPENAI_API_KEY를 입력해주세요!")
    st.stop()

# client 설정 시 base_url을 추가해야 합니다.
client = OpenAI(base_url='https://gms.ssafy.io/gmsapi/api.openai.com/v1')


# --- 기능 함수 정의 ---

def get_google_news(keyword):
    """[F03] RSS 뉴스 수집"""
    rss_url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    return [{"title": e.title, "link": e.link} for e in feed.entries[:3]] # 3개만 수집

def process_ai_logic(user_input):
    """[F05] 의도 판별 및 [F04] 요약"""
    try:
        # 1. 의도 판별
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "뉴스 검색이면 'SEARCH: 키워드'라고 답하고, 아니면 친절히 대화하세요."},
                {"role": "user", "content": user_input}
            ]
        )
        ai_msg = response.choices[0].message.content

        if "SEARCH:" in ai_msg:
            keyword = ai_msg.split("SEARCH:")[1].strip()
            news_items = get_google_news(keyword)
            
            if not news_items:
                return f"'{keyword}' 뉴스 결과가 없습니다."
            
            # 2. 요약 생성
            result = f"### 📰 '{keyword}' 뉴스 요약\n\n"
            for item in news_items:
                # 기사 제목 요약 (바이브 코딩: 제목만으로 요약 시도)
                sum_res = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": f"이 제목 요약해줘: {item['title']}"}]
                )
                summary = sum_res.choices[0].message.content
                result += f"- **{item['title']}**\n  - 요약: {summary}\n  - [링크]({item['link']})\n\n"
            return result
        else:
            return ai_msg
    except Exception as e:
        return f"❌ 오류 발생: {str(e)}"

# --- 채팅 인터페이스 ---

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("뉴스 키워드나 궁금한 점을 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            answer = process_ai_logic(prompt)
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})