import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime
import japanize_matplotlib
import seaborn as sns

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
	query = f"SELECT {column_name} FROM {table_name} ORDER BY rowid DESC LIMIT 168"
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
plt.tight_layout()
# sns.set(style="whitegrid")
sns.set()

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
# plt.title('temperature')
plt.xticks(rotation=20)
plt.ylabel('temperature[℃]')
plt.grid(True)
plt.plot(x, y, 
	# marker='o', 
	# linestyle='None',
	markerfacecolor='red')
	# markeredgecolor='red')
am_x = []
am_y = []
pm_x = []
pm_y = []
for i, date in enumerate(x):
	if date.hour < 12:
		am_x.append(date)
		am_y.append(y[i])
	else:
		pm_x.append(date)
		pm_y.append(y[i])
plt.scatter(am_x, am_y, color='chocolate', marker='o', label='AM')
plt.scatter(pm_x, pm_y, color='indigo', marker='o', label='PM')
 #plt.bar(am_x, am_y, color='chocolate', label='AM')
# plt.bar(pm_x, pm_y, color='indigo', label='PM')
plt.legend()
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image1.jpg')
plt.clf()
print('created image1')

# 湿度グラフの作成
x = new_timestamp
humidity = fetch_recent_data(db_path, table_name, column_humidity)
y = humidity
# plt.title('humidity')
plt.plot(x,y)
plt.xticks(rotation=20)
plt.ylabel('humidity[%]')
plt.grid(True)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image2.jpg')
plt.clf()
print('created image2')

# 気圧グラフの作成
x = new_timestamp
pressure = fetch_recent_data(db_path, table_name, column_pressure)
y = pressure
# plt.title('pressure')
plt.plot(x,y)
plt.xticks(rotation=20)
plt.ylabel('pressure[hPa]')
plt.grid(True)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image3.jpg')
plt.clf()
print('created image3')

# 人工衛星の捕捉数グラフの作成
x = new_timestamp
satellite_count = fetch_recent_data(db_path, table_name, column_satelliteCount)
y = satellite_count
# plt.title('satellite_count')
plt.plot(x,y)
plt.xticks(rotation=20)
plt.ylabel('satellite_count')
plt.grid(True)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image4.jpg')
plt.clf()
print('created image4')

# 不快指数
T = np.array(tempture)
H = np.array(humidity)
discomfort_index = 0.81 * T + 0.01* H * (0.99 * T -14.3) + 46.3
discomfort_index_avg = str(int(np.mean(discomfort_index)))
# print(discomfort_index_avg)
print(f"不快指数：{discomfort_index_avg}")

# 体感温度

# htmlの書き換え
html_file_path = "index.html"
with open(html_file_path, "r") as file:
	html_content = file.read()

html_content = html_content.replace("{placeholder6}", discomfort_index_avg)

with open(html_file_path, "w") as file:
	file.write(html_content)


# plt.show()













