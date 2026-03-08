import pandas as pd
import numpy as np

# 1. 고객정보 (Customer Info)
customer_data = {
    '고객ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
    '이름': ['김철수', '이영희', '박민수', '최지우', '정다은'],
    '지역': ['서울', '부산', '대구', '인천', '광주'],
    '가입일': ['2023-01-15', '2023-03-22', '2023-05-10', '2023-08-05', '2023-11-12']
}
df_customers = pd.DataFrame(customer_data)

# 2. 구매정보 (Purchase Info)
purchase_data = {
    '주문ID': ['P1001', 'P1002', 'P1003', 'P1004', 'P1005', 'P1006'],
    '고객ID': ['C001', 'C003', 'C002', 'C001', 'C005', 'C004'],
    '상품명': ['노트북', '마우스', '모니터', '키보드', '태블릿', '헤드셋'],
    '수량': [1, 2, 1, 1, 1, 2],
    '금액': [1200000, 25000, 300000, 80000, 600000, 150000],
    '구매일': ['2024-01-02', '2024-01-05', '2024-01-10', '2024-02-15', '2024-02-20', '2024-03-01']
}
df_purchases = pd.DataFrame(purchase_data)

# 3. 재고정보 (Inventory Info)
inventory_data = {
    '상품ID': ['I001', 'I002', 'I003', 'I004', 'I005', 'I006'],
    '상품명': ['노트북', '마우스', '모니터', '키보드', '태블릿', '헤드셋'],
    '카테고리': ['가전', '주변기기', '가전', '주변기기', '가전', '주변기기'],
    '현재고': [15, 120, 25, 45, 10, 60],
    '입고가': [900000, 15000, 220000, 50000, 450000, 100000]
}
df_inventory = pd.DataFrame(inventory_data)

# 엑셀 파일로 저장
file_name = 'dashboard_sample_data.xlsx'
with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
    df_customers.to_excel(writer, sheet_name='고객정보', index=False)
    df_purchases.to_excel(writer, sheet_name='구매정보', index=False)
    df_inventory.to_excel(writer, sheet_name='재고정보', index=False)

print(f"'{file_name}' 파일이 성공적으로 생성되었습니다.")
