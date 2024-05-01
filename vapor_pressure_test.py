import math

T = 10  # 摂氏
RH = 77  # 相対湿度

print(f"温度：{T}")

def calc_dew_point(T, RH):
	# 露点温度の算出
	b = 17.62
	c = 243.12
	gamma = (b * T / (c + T)) + math.log(RH / 100.0)
	T_dew = (c * gamma) / (b - gamma)
	return T_dew

def calc_saturation_vapor_pressure(T_dew):
	# 露点温度を引数にして水蒸気圧を算出
	e = 6.1078 * 10 ** (7.5 * T_dew /(237.3 + T_dew))
	return e

def calc_humidex(T, e):
	# カナダ気象局(MSC)
	humidex = T + 0.5555 * (e - 10)
	humidex = int(humidex)
	return humidex

dew_point = calc_dew_point(T, RH)
print(f"露点温度：{dew_point}")

e = calc_saturation_vapor_pressure(dew_point)
print(f"水蒸気圧：{e}")

humidex = calc_humidex(T, e)
print(f"体感温度：{humidex}")
