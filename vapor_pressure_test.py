import numpy as np

T = np.array([10, 15, 20, 25])  # 摂氏
RH = np.array([20, 40, 60, 80])  # 相対湿度

print(f"温度：{T}")

def calc_dew_point(T, RH):
	# マグヌスの式
	# 露点温度の算出
	b = 17.62
	c = 243.12
	gamma = (b * T / (c + T)) + np.log(RH / 100.0)
	T_dew = (c * gamma) / (b - gamma)
	return T_dew

def calc_saturation_vapor_pressure(T_dew):
	# テトンスの式
	# 露点温度を引数にして水蒸気圧を算出
	e = 6.1078 * 10 ** (7.5 * T_dew /(237.3 + T_dew))
	return e

def calc_humidex(T, e):
	# カナダ気象局(MSC)
	humidex = T + 0.5555 * (e - 10)
	humidex = np.floor(humidex)
	humidex = humidex.astype(int)
	return humidex

def wagner_vapor_pressure(T):
	T_k = T + 273.15
	
	T_c = 647.096  # 臨界温度
	P_c = 220640  # 臨界圧
	a1 = -7.85951783
	a2 = 1.84408259
	a3 = -11.7866497
	a4 = 22.6807411
	a5 = -15.9618719
	a6 = 1.80122502
	
	Tr = T_k / T_c  # 減温比
	tau = 1 - Tr
	ln_Ps = T_c / T_k * (a1 * tau 
		+ a2 * tau**1.5 
		+ a3 * tau**3 
		+ a4 * tau**3.5 
		+ a5 * tau**4 
		+ a6 * tau**7.5)
	Ps = np.exp(ln_Ps) * P_c
	
	e = Ps / 100
	
	return e

def wagner_temperature(RH, Ps):
	Pv = (RH / 100) * Ps
	return Pv

dew_point = calc_dew_point(T, RH)
print(f"露点温度：{dew_point}")

e = calc_saturation_vapor_pressure(dew_point)
print(f"テトンス：水蒸気圧：{e}")

humidex = calc_humidex(T, e)
print(f"体感温度：{humidex}")

wagner_press = wagner_vapor_pressure(T)
print(f"ワグナー水蒸気圧：{wagner_press}")

wagner_temp = wagner_temperature(RH, wagner_press)
print(f"ワグナー露点温度：{wagner_temp}")



