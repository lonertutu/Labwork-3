import matplotlib.pyplot as plt
import numpy as np


plt.subplots(figsize=(16, 10), dpi = 100)

y = []
pressure = open("00Pa.txt", "r")
i = 1
for line in pressure:
    if i >= 9:
        y.append(int(line))
    i += 1
meanv = np.mean(y)
plt.suptitle("Калибровочный график зависимости показаний АЦП от давления")
plt.xlabel("Давление [Па]")
plt.ylabel("Отсчеты АЦП")
plt.grid(True, which = "major", linestyle = "-")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.plot(y, label = "P = {:.3f} * (N - {}) [Па]".format(50/300, meanv))
legend = plt.legend(loc='upper left', fontsize='large')

plt.savefig("pressure-calibration.png")
plt.show()