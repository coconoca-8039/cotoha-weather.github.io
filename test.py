import sqlite3

# このファイルからhtmlに対してwrite処理をする
# その後は、別に作るシェルファイルでcommitをする

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
		data = float(row[0])
		data_list.append(data)
	
	con.close()
	
	return data_list

db_path = "/home/pi/Desktop/rasp-project/ClimateData.db"
table_name = "ClimateData"
column_tempture = "Temperature"
column_humidity = "Humidity"
column_pressure = "Pressure"
column_satelliteCount = "SatelliteCount"

tempture = fetch_recent_data(db_path, table_name, column_tempture)
tempture_disp = round(sum(tempture) / len(tempture), 2)

humidity = fetch_recent_data(db_path, table_name, column_humidity)
humidity_disp = round(sum(humidity) / len(humidity), 2)

pressure = fetch_recent_data(db_path, table_name, column_pressure)
pressure_disp = round(sum(pressure) / len(pressure), 2)

satellite_count = fetch_recent_data(db_path, table_name, column_satelliteCount)
satellite_count_disp = round(sum(satellite_count) / len(satellite_count), 2)

print(f"気温：{round(sum(tempture) / len(tempture), 2)}")
print(f"湿度：{round(sum(humidity) / len(humidity), 2)}")
print(f"気圧：{round(sum(pressure) / len(pressure), 2)}")
print(f"衛星：{round(sum(satellite_count) / len(satellite_count), 2)}")

