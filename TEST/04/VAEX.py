#VAEX.py
import vaex
# 대용량 데이터셋 불러오기
df = vaex.example()

# 데이터의 처음 몇 줄 출력
print(df.head())

# 데이터 요약 통계 출력
print(df.describe())

# 데이터 필터링 및 새 컬럼 생성
filtered_df = df[df.x < 0]
filtered_df['x_squared'] = filtered_df.x**2

# 결과 출력
print(filtered_df.head())