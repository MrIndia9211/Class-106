import csv
import plotly.express as px 


with open('2.csv') as csv_file :
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x='Coffee',y='sleep')
    fig.show()