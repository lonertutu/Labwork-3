import matplotlib.pyplot as plt
import numpy as np
import math
with open(r"C:\Users\Arina\Desktop\py\X.txt", "r") as settings:
    X = [float(i) for i in settings.read().split("\n")]


y0 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []

f00 = open("00.txt", "r")
f10 = open("10.txt", "r")
f20 = open("20.txt", "r")
f30 = open("30.txt", "r")
f40 = open("40.txt", "r")
f50 = open("50.txt", "r")
f60 = open("60.txt", "r")
f70 = open("70.txt", "r")

i = 1
for line in f00:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y0.append(a)
    i += 1
i = 1
for line in f10:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y1.append(a)
    i += 1
i = 1
for line in f20:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y2.append(a)
    i += 1
i = 1
for line in f30:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y3.append(a)
    i += 1
i = 1
for line in f40:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y4.append(a)
    i += 1
i = 1
for line in f50:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y5.append(a)
    i += 1
i = 1
for line in f60:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y6.append(a)
    i += 1
i = 1
for line in f70:
    if i >= 9:
        if(int(line) >= 812):
            a = (math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
            if(a<4):
                a=3
            y7.append(a)
    i += 1

yy0 = y0.index(max(y0)) - 50
if(yy0>=0):
    y0 = y0[yy0:] + [3]*yy0
else:
    yy0 = abs(yy0)
    y0 = [3]*yy0 + y0[0:(100-yy0)]

yy1 = y1.index(max(y1)) - 50
if(yy1>=0):
    y1 = y1[yy1:] + [3]*yy1
else:
    yy1 = abs(yy1)
    y1 = [3]*yy1 + y1[0:(100-yy1)]

yy2 = y2.index(max(y2)) - 50
if(yy2>=0):
    y2 = y2[yy2:] + [3]*yy2
else:
    yy2 = abs(yy2)
    y2 = [3]*yy2 + y2[0:(100-yy2)]

yy3 = y3.index(max(y3)) - 50
if(yy3>=0):
    y3 = y3[yy3:] + [3]*yy3
else:
    yy3 = abs(yy3)
    y3 = [3]*yy3 + y3[0:(100-yy3)]  

yy4 = y4.index(max(y4)) - 50
if(yy4>=0):
    y4 = y4[yy4:] + [3]*yy4
else:
    yy4 = abs(yy4)
    y4 = [3]*yy4 + y4[0:(100-yy4)]

yy5 = y5.index(max(y5)) - 50
if(yy5>=0):
    y5 = y5[yy5:] + [3]*yy5
else:
    yy5 = abs(yy5)
    y5 = [3]*yy5 + y5[0:(100-yy5)]

yy6 = y6.index(max(y6)) - 50
if(yy6>=0):
    y6 = y6[yy6:] + [3]*yy6
else:
    yy6 = abs(yy6)
    y6 = [3]*yy6 + y6[0:(99-yy6)]

yy7 = y7.index(max(y7)) - 50
if(yy7>=0):
    y7 = y7[yy7:] + [3]*yy7
else:
    yy7 = abs(yy7)
    y7 = [3]*yy7 + y7[0:(100-yy7)]


fig, ax = plt.subplots(figsize=(16, 10), dpi = 100)
fig.suptitle("Скорость потока воздуха в сечении затопленной струи")
ax.plot(X, y0, lw = 1, c = "black", label = "Q (00mm) = ")
ax.plot(X, y1, lw = 1, c = "green", label = "Q (10mm) = ")
ax.plot(X, y2, lw = 1, c = "red", label = "Q (20mm) = ")
ax.plot(X, y3, lw = 1, c = "brown", label = "Q (30mm) = ")
ax.plot(X, y4, lw = 1, c = "orange", label = "Q (40mm) = ")
ax.plot(X, y5, lw = 1, c = "cyan", label = "Q (50mm) = ")
ax.plot(X, y6, lw = 1, c = "purple", label = "Q (60mm) = ")
ax.plot(X, y7, lw = 1, c = "lime", label = "Q (70mm) = ")

legend = ax.legend(loc='upper right', fontsize='medium')

plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.ylabel("Скорость воздуха [м/с]")
#plt.text(30, 1.2, "Время зарядки = 49.3с")
#plt.text(30, 0.75, "Время разрядки = 40.7с")
plt.grid(True, which = "major", linestyle = "-")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
#ax.axis([0, 90, 0, 3.5])
fig.savefig("velocity-outgo-uncentered.png")
plt.show()



