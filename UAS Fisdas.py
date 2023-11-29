import matplotlib.pyplot as plt
from prettytable import PrettyTable

# data massa kendaraan dalam (kg)
ayla = 800
avanza = 1100
fortuner = 1500
minivan = 1800
bus = 2200

# data percepataan tiap kendaraan dalam (m/s^2)
percepatan1 = 30
percepatan2 = 45
percepatan3 = 60
percepatan4 = 75
percepatan5 = 90

# Waktu awal tabrakan yaitu 0
waktu_awal = 0
# Perubahan Waktu  (detik)
waktu1 = 0.10
waktu2 = 0.12
waktu3 = 0.15
waktu4 = 0.17
waktu5 = 0.21

# gaya dengan rumus (F = massa * percepatan)
gaya1 = ayla * percepatan1
gaya2 = avanza *  percepatan2
gaya3 = fortuner * percepatan3
gaya4 = minivan * percepatan4
gaya5 = bus * percepatan5

# impuls dengan menggunakan rumus integral
impuls1 = (gaya1 * waktu1)
impuls2 = (gaya2 * waktu2)
impuls3 = (gaya3 * waktu3)
impuls4 = (gaya4 * waktu4)
impuls5 = (gaya5 * waktu5)

# Nama kolom
tabel = PrettyTable(["Mobil","Massa (kg)","Percepatan (m/s^2)","Gaya (F)","Waktu Tabrakan (s)","Impuls (N.s)"])

# Data tabel
tabel.add_row(["Ayla",ayla,percepatan1,gaya1,waktu1,impuls1])
tabel.add_row(["Avanza",avanza,percepatan2,gaya2,waktu2,impuls2])
tabel.add_row(["Fortuner",fortuner,percepatan3,gaya3,waktu3,impuls3])
tabel.add_row(["Minivan",minivan,percepatan4,gaya4,waktu4,impuls4])
tabel.add_row(["Bus",bus,percepatan5,gaya5,waktu5,impuls5])
print(tabel)

# Grafik
plt.plot([gaya1,gaya2,gaya3,gaya4,gaya5], [waktu1, waktu2, waktu3, waktu4, waktu5])
plt.scatter([gaya1],[waktu1], color='red', label = 'Ayla')
plt.scatter([gaya2],[waktu2], color='blue', label = 'Avanza')
plt.scatter([gaya3],[waktu3], color='green', label = 'Fortuner')
plt.scatter([gaya4],[waktu4], color='orange', label = 'Minivan')
plt.scatter([gaya5],[waktu5], color='magenta', label = 'Bus')
plt.title('Impuls Terhadap Waktu')
plt.xlabel('Gaya Yang Terjadi(F)')
plt.ylabel('Waktu Tabrakan (s)')
plt.legend()
plt.show()
