import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#particular terms that are popular in the region around the world
trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10))

#visualize the above search results
df = data.sample(10)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(120,16), kind="bar")
plt.show()

#top daily 10 search trends in India
data = trends.trending_searches(pn="india")
print(data.head(10))

