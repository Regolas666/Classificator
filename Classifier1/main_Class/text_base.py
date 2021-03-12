import sqlite3
#from .models import New

conn = sqlite3.connect("table_of_news.db")
cursor = conn.cursor()
news_base = []
sql = "SELECT * FROM texts"
cursor.execute(sql)
result_sql = cursor.fetchall()
for k in range(1000):
    news_base.append(result_sql[k])
    print(news_base[k])
