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
	query = f"SELECT {column_name} FROM {table_name} ORDER BY rowid DESC LIMIT 10"
	cursor.execute(query)
	
	# 結果をリストに格納
	# recent_data = cursor.fetchall()
	#data_list = [float(row[0]) for row in cursor.fetchall()]
	data_list = []
	for row in cursor.fetchall():
		if column_name != column_timestamp:
			data = float(row[0])
		data_list.append(row[0])
	
	con.close()
	
	return data_list

print("------------")

tempture = fetch_recent_data(db_path, table_name, column_tempture)
print(tempture)
timestamp = fetch_recent_data(db_path, table_name, column_timestamp)
print(timestamp)
print(type(timestamp[0]))

plt.figure(figsize=(10, 10))
plt.rcParams.update({'font.size':20})

def test():
	x = [1, 2, 3, 4, 5, 6, 7]
	y = [1, 4, 9, 16, 25, 36, 49]
	plt.title('1')
	plt.plot(y, x)
	plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image1.jpg')
	plt.clf()

	x = [1, 2, 3, 4, 5, 6, 7]
	y = np.array(x) ** 2
	plt.title('2')
	plt.plot(x,y)
	plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image2.jpg')
	plt.clf()

	x = [1, 2, 3, 4, 5, 6, 7]
	y = np.array(x) ** 3
	plt.title('3')
	plt.plot(x,y)
	plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image3.jpg')
	plt.clf()

	x = [1, 2, 3, 4, 5, 6, 7]
	y = [7, 6, 5, 4, 3, 2, 1]
	plt.title('4')
	plt.plot(x,y)
	plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image4.jpg')
	plt.clf()

	# plt.show()
