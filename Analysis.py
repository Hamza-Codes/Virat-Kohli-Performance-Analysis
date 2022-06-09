import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('Dataset.csv')
print(data.head())

# Let’s have a look at whether this dataset contains any null values or not before moving forward:

print(data.isnull().sum())

# The dataset contains matches played by Virat Kohli between 18 August 2008 and 22 January 2017. So let’s have a look at the total runs scored by Virat Kohli:

print('Total Runs',data['Runs'].sum())

print('Average Runs',data['Runs'].mean())

matches = data.index
figure = px.line(data, x=matches, y = "Runs", title = "Run scored by Virat Kohli between 18 Aug, 2008 and 22-Jan-17. ")
figure.show()

pos = data['Pos'].value_counts()
labels = pos.index
counts = pos.values
colors = ['gold','lightgreen','pink', 'blue', 'skyblue', 'cyan', 'orange']
fig = go.Figure(data=[go.Pie(labels = labels, values = counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()

figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
            title="Most Runs Against Teams")
figure.show()

figure = px.bar(centuries, x=centuries["Opposition"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Most Centuries Against Teams")
figure.show()

strike_rate = data.query("SR >= 120")
print(strike_rate)

figure = px.bar(strike_rate, x = strike_rate["Inns"], 
                y = strike_rate["SR"], 
                color = strike_rate["SR"],
            title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
figure.show()

figure = px.scatter(data_frame = data, x="Runs",
                    y="4s", size="SR", trendline="ols", 
                    title="Relationship Between Runs Scored and Fours")
figure.show()

figure = px.scatter(data_frame = data, x="Runs",
                    y="6s", size="SR", trendline="ols", 
                    title= "Relationship Between Runs Scored and Sixes")
figure.show()