# Google Search Analysis

As the heading describes, this task involves analyzing the queries that are searched in Google Search using Google Trends. This report mainly explains each line of code and its purpose.

`pip install pytrends`

pytrends library is used to interact with the Google Trends API. This line is used to install pytrends.

```python
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
```
These lines import the necessary libraries: **pandas** for data manipulation, **TrendReq** from pytrends.request for making requests to the Google Trends API, and **matplotlib.pyplot** for data visualization.

`trends = TrendReq()`

It creates an instance of the TrendReq class from the pytrends library. This instance is used to make requests to the Google Trends API.

```python
query = input("Enter the keyword to analyze: ")
trends.build_payload(kw_list = [query])
```
This builds the payload for the query by specifying the keyword(s) to search for in the kw_list parameter of the build_payload method. The desired keyword to be analyzed is stored in the variable **query**. Here the keyword "data analysis" has been analyzed.

`data = trends.interest_by_region()`

This retrieves the interest by region data for the specified query using the interest_by_region method of the trends instance. 

`data = data.sort_values(by = query, ascending = False)`

This sorts the data DataFrame by the interest values of the specified query in descending order. The **by** parameter specifies the column to sort by.

```python
data = data.head(25)
print(data)
```
This selects the top 25 rows from the sorted data DataFrame, representing the regions with the highest interest in the specified query.
![list](/screenshots/list.png)

`data.reset_index().plot(x = "geoName", y = query, kind = "bar")`

This creates a bar plot using the plot function of the data DataFrame. The reset_index method is used to reset the index of the DataFrame, and x and y parameters specify the columns to use for the x-axis and y-axis of the plot.

```python
plt.style.use('fivethirtyeight')
plt.show()
```
These lines set the plot style to 'fivethirtyeight', a predefined style from matplotlib, and display the plot on the screen.
![bar_chart](/screenshots/bar_chart.png)

```python
data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=[query])
data = data.interest_over_time()
```

These lines create a new instance of the **TrendReq** class, build the payload for the query, and retrieve the historical interest over time data for the specified query using the **interest_over_time** method. The resulting data is assigned to the data variable.

`fig, ax = plt.subplots(figsize=(15, 12))`

This creates a new figure and axes for the plot. The **figsize** parameter sets the size of the figure in inches, specifying its width and height.

`data[query].plot()`

This line plots the historical interest values from the data DataFrame for the specified query. The **data[query]** syntax selects the column corresponding to the specified query, and the .plot() method creates the line plot.

```python
plt.style.use('fivethirtyeight')
plt.title(f'Total Google Searches for: {query}', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
```
These lines set the plot style to 'fivethirtyeight', set the title, x-axis label, and y-axis label for the plot, and display the plot on the screen.
![trends](/screenshots/trends.png)

## Reference
- __[Search Analysis](https://thecleverprogrammer.com/2021/04/27/google-search-analysis-with-python/)__
