import matplotlib.pyplot as plt
import numpy as np

y = np.loadtxt("distance-calibration.txt", dtype = float)
x = np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900])


plt.subplots(figsize=(16, 10), dpi = 100)

A = np.vstack([x, np.ones(len(x))]).T
dx, dy = np.linalg.lstsq(A, y, rcond=None)[0]

plt.suptitle("Калибровочный график зависимости перемещений трубки Пито от шага двигателя")
plt.xlabel("Количество шагов")
plt.ylabel("Перемещение трубки Пито [м]")
plt.grid(True, which = "major", linestyle = "-")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.plot(x, y, label = "x = {:.5f} * step [мм]".format(dx))
legend = plt.legend(loc='upper left', fontsize='large')

plt.savefig("distance-calibration.png")
plt.show()