# 🤖 AI 뉴스 요약 비서 (News Summary Bot)

> **"복잡한 세상, 뉴스 요약으로 한눈에 파악하세요!"** > OpenAI의 강력한 AI를 활용하여 사용자가 원하는 키워드의 실시간 뉴스를 검색하고, 핵심 내용을 3줄로 요약해주는 서비스입니다.

---

## 🌟 주요 기능
- **실시간 뉴스 검색**: Naver 뉴스 API(또는 관련 도구)를 통해 실시간 데이터를 수집합니다.
- **AI 핵심 요약**: GPT-4o-mini 모델을 사용하여 방대한 기사 내용을 간결하게 요약합니다.
- **사용자 맞춤 UI**: 하늘색 테마의 깔끔한 디자인으로 가독성을 높였습니다.
- **웹 배포**: Streamlit Cloud를 통해 어디서나 접속 가능한 URL을 제공합니다.

## 🛠 기술 스택
- **Language**: Python 3.x
- **Framework**: Streamlit
- **AI Library**: OpenAI API, LangChain
- **Deployment**: GitHub, Streamlit Cloud

## 📂 폴더 구조
```text
news-summary-bot/
├── .streamlit/
│   └── config.toml       # 사이트 테마 및 디자인 설정
├── app.py                # 챗봇 메인 로직 코드
├── requirements.txt      # 실행을 위한 라이브러리 목록
└── README.md             # 프로젝트 설명서

🔒 보안 및 설정 (Security)
본 프로젝트는 보안을 위해 다음과 같은 설정을 적용하였습니다.

API Key 관리: .env 파일을 통해 로컬 환경을 보호하고, 배포 시에는 GitHub Secrets를 사용하여 API 키 유출을 원천 차단했습니다.

배포 환경 설정: Streamlit Cloud의 Advanced Settings를 통해 환경 변수를 안전하게 관리합니다.
