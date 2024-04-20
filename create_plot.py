import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("kotoha")

plt.figure(figsize=(10, 10))

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 9, 16, 25, 36, 49]
plt.title('1')
plt.plot(y, x)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image1.jpg')

x = [1, 2, 3, 4, 5, 6, 7]
y = np.array(x) ** 2
plt.title('2')
plt.plot(x,y)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image2.jpg')

x = [1, 2, 3, 4, 5, 6, 7]
y = np.array(x) ** 3
plt.title('3')
plt.plot(x,y)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image3.jpg')

x = [1, 2, 3, 4, 5, 6, 7]
y = [7, 6, 5, 4, 3, 2, 1]
plt.title('4')
plt.plot(x,y)
plt.savefig('/home/pi/Desktop/cotoha/cotoha-weather.github.io/image4.jpg')

# plt.show()
