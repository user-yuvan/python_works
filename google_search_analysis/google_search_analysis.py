#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pytrends.request import TrendReq # pytrends is the library that is used to receive data from GoogleTrends
import matplotlib.pyplot as plt
trends = TrendReq()


# In[ ]:


query = input("Enter the keyword to analyze: ")
trends.build_payload(kw_list = [query])
data = trends.interest_by_region()
data = data.sort_values(by = query, ascending = False)
data = data.head(25)
print(data)


# In[ ]:


# To visualize the data using bar chart
data.reset_index().plot(x = "geoName", y = query, kind = "bar")
plt.style.use('fivethirtyeight')
plt.show()


# In[ ]:


# trends of the search query
data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=[query])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data[query].plot()
plt.style.use('fivethirtyeight')
plt.title(f'Total Google Searches for: {query}', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

