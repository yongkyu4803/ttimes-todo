import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="고객 구매 내역 대시보드", layout="wide")

# 데이터 로드 함수
@st.cache_data
def load_data(file_path):
    customers = pd.read_excel(file_path, sheet_name='고객정보')
    purchases = pd.read_excel(file_path, sheet_name='구매정보')
    inventory = pd.read_excel(file_path, sheet_name='재고정보')
    return customers, purchases, inventory

try:
    file_path = 'dashboard_sample_data.xlsx'
    df_customers, df_purchases, df_inventory = load_data(file_path)

    st.title("🛍️ 고객 구매 내역 및 통계 대시보드")
    st.markdown("---")

    # 사이드바: 고객 선택
    st.sidebar.header("고객 선택")
    customer_list = df_customers['이름'].tolist()
    selected_customer_name = st.sidebar.selectbox("고객 이름을 선택하세요:", customer_list)

    # 선택된 고객 정보 추출
    customer_info = df_customers[df_customers['이름'] == selected_customer_name].iloc[0]
    customer_id = customer_info['고객ID']

    # 레이아웃 구성: 상단 요약 지표
    col1, col2, col3 = st.columns(3)

    # 고객별 구매 내역 필터링
    customer_purchases = df_purchases[df_purchases['고객ID'] == customer_id]
    total_spent = customer_purchases['금액'].sum()
    total_count = len(customer_purchases)

    with col1:
        st.subheader("👤 고객 프로필")
        st.write(f"**이름:** {customer_info['이름']}")
        st.write(f"**아이디:** {customer_info['고객ID']}")
        st.write(f"**지역:** {customer_info['지역']}")
        st.write(f"**가입일:** {customer_info['가입일']}")

    with col2:
        st.metric("총 구매 금액", f"{total_spent:,} 원")
    
    with col3:
        st.metric("총 구매 건수", f"{total_count} 건")

    st.markdown("---")

    # 상세 내역 및 차트 레이아웃
    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.subheader("📄 상세 구매 내역")
        if not customer_purchases.empty:
            st.dataframe(customer_purchases[['주문ID', '상품명', '수량', '금액', '구매일']], use_container_width=True)
        else:
            st.warning("구매 내역이 없습니다.")

    with right_col:
        st.subheader("📊 상품별 구매 비중")
        if not customer_purchases.empty:
            fig = px.pie(customer_purchases, values='금액', names='상품명', title=f"{selected_customer_name}님의 상품별 지출")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("차트를 표시할 데이터가 없습니다.")

    # 전체 통계 섹션 (선택 사항)
    st.markdown("---")
    if st.checkbox("전체 구매 통계 보기"):
        st.subheader("📈 전체 상품 판매 순위")
        total_sales = df_purchases.groupby('상품명')['금액'].sum().sort_values(ascending=False).reset_index()
        fig_total = px.bar(total_sales, x='상품명', y='금액', color='상품명', title="전체 상품 매출 현황")
        st.plotly_chart(fig_total, use_container_width=True)

except FileNotFoundError:
    st.error(f"'{file_path}' 파일을 찾을 수 없습니다. 먼저 `generate_sample_data.py`를 실행하여 데이터를 생성해 주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
