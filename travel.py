import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

travel = pd.read_excel("C:/Users/USER/Documents/LS빅데이터스쿨/LsBigdata-project1/data/travel.xlsx")
travel


# 행 이름 바꾸기
travel = travel.rename(columns = {"소계" : "total", "년":"year", "월":"month"})
travel.head()


# 25000횟수 이상 여행한 월
travel.query("total > 25000")


# total 여행 횟수 오름 차순 정리
travel.sort_values(["month","total"], ascending = [True,False])

# 연도 별 평균 여행 횟수
travel.groupby("year")\
      .agg(mean_travel=("total", "mean"))
      
# 연도 및 월별 평균 여행 횟수
travel.groupby(["year","month"])\
      .agg(mean_travel=("total", "mean"))
  
# total이 25000이상인 것에 Good
travel["Good_Bad"] = np.where(travel["total"]>=25000, "Good" , "Bad")
travel["Good_Bad"].value_counts()


# 연도별 그래프 확인하기
df_year = travel.groupby("year")\
          .agg(mean_travel=("total", "mean"))
plt.clf()
df_year.plot.bar(rot=0)
plt.show()
