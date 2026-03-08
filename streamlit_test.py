import streamlit as st

# 페이지 타이틀 설정
st.set_page_config(page_title="스트림릿 설치 테스트")

# 텍스트 출력
st.title("스트림릿 설치 테스트")
st.success("안녕하세요. 스트림릿이 제대로 설치됐습니다.")

# 추가 정보 (선택 사항)
st.info("터미널에서 `streamlit run streamlit_test.py`를 실행하여 확인하세요.")
