import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

db_path = "/home/pi/Desktop/rasp-project/ClimateData.db"
table_name = "ClimateData"
column_tempture = "Temperature"
column_humidity = "Humidity"
column_pressure = "Pressure"
column_satelliteCount = "SatelliteCount"
column_timestamp = "Timestamp"

def fetch_recent_data(db_path, table_name, column_name):
	
	# SQLiteデータベースに接続
	con = sqlite3.connect(db_path)
	cursor = con.cursor()
	
	# 最新データを参照
	# query = f"SELECT * FROM {table_name} ORDER BY Timestamp DESC LIMIT {limit}"
	query = f"SELECT {column_name} FROM {table_name} ORDER BY rowid DESC LIMIT 96"
	cursor.execute(query)
	
	# 結果をリストに格納
	# recent_data = cursor.fetchall()
	#data_list = [float(row[0]) for row in cursor.fetchall()]
	data_list = []
	for row in cursor.fetchall():
		if column_name != column_timestamp:
			data = float(row[0])
			data_list.append(data)
		else:
			data_list.append(row[0])
	
	con.close()
	
	return data_list
	
plt.figure(figsize=(10, 10))
plt.rcParams.update({'font.size':15})	

# 気温グラフの作成
tempture = fetch_recent_data(db_path, table_name, column_tempture)
new_timestamp = []
timestamp = fetch_recent_data(db_path, table_name, column_timestamp)
for date_str in timestamp:
	# date_str = date_str[5:]
	date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
	new_timestamp.append(date_obj)

x = new_timestamp
y = tempture
plt.title('temperature')
plt.plot(x, y)
plt.xticks(rotation=20)
plt.xlabel('date')
plt.ylabel('temperature')
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image1.jpg')
plt.clf()

# 湿度グラフの作成
x = new_timestamp
humidity = fetch_recent_data(db_path, table_name, column_humidity)
y = humidity
plt.title('humidity')
plt.plot(x,y)
plt.xlabel('date')
plt.ylabel('humidity')
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image2.jpg')
plt.clf()

# 気圧グラフの作成
x = new_timestamp
pressure = fetch_recent_data(db_path, table_name, column_pressure)
y = pressure
plt.title('pressure')
plt.plot(x,y)
plt.xlabel('date')
plt.ylabel('pressure')
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image3.jpg')
plt.clf()

# 人工衛星の捕捉数グラフの作成
x = new_timestamp
satellite_count = fetch_recent_data(db_path, table_name, column_satelliteCount)
y = satellite_count
plt.title('satellite_count')
plt.plot(x,y)
plt.xlabel('date')
plt.ylabel('satellite_count')
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image4.jpg')
plt.clf()

# plt.show()
