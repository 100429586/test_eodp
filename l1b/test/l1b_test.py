import matplotlib.pyplot as plt
import numpy as np

#poner los plots que piden
from common.io.writeToa import readToa
l1b_toa0=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs','l1b_toa_VNIR-0.nc')
l1b_toa1=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs','l1b_toa_VNIR-1.nc')
l1b_toa2=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs','l1b_toa_VNIR-2.nc')
l1b_toa3=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs','l1b_toa_VNIR-3.nc')

l1b_toa0_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\output','l1b_toa_VNIR-0.nc')
l1b_toa1_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\output','l1b_toa_VNIR-1.nc')
l1b_toa2_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\output','l1b_toa_VNIR-2.nc')
l1b_toa3_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\output','l1b_toa_VNIR-3.nc')

ism_toa_isrf0=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-0.nc')
ism_toa_isrf1=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-1.nc')
ism_toa_isrf2=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-2.nc')
ism_toa_isrf3=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-3.nc')

l1b_toa0_noeq=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq','l1b_toa_VNIR-0.nc')
l1b_toa1_noeq=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq','l1b_toa_VNIR-1.nc')
l1b_toa2_noeq=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq','l1b_toa_VNIR-2.nc')
l1b_toa3_noeq=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq','l1b_toa_VNIR-3.nc')


# Calcular diferencias relativas
#   Diferencia relativa en porcentaje
diff0 = (l1b_toa0 - l1b_toa0_original) / l1b_toa0_original * 100
diff1 = (l1b_toa1 - l1b_toa1_original) / l1b_toa1_original * 100
diff2 = (l1b_toa2 - l1b_toa2_original) / l1b_toa2_original * 100
diff3 = (l1b_toa3 - l1b_toa3_original) / l1b_toa3_original * 100

print(f"La diferencia en la banda 0 es: \n {diff0}")
print(f"La diferencia en la banda 1 es: \n {diff1}")
print(f"La diferencia en la banda 2 es: \n {diff2}")
print(f"La diferencia en la banda 3 es: \n {diff3}")


x = np.arange(150)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # 2 filas, 2 columnas

datasets = [
    (l1b_toa0, ism_toa_isrf0, "toa0 vs isrf0"),
    (l1b_toa1, ism_toa_isrf1, "toa1 vs isrf1"),
    (l1b_toa2, ism_toa_isrf2, "toa2 vs isrf2"),
    (l1b_toa3, ism_toa_isrf3, "toa3 vs isrf3"),
]

for ax, (toa, isrf, title) in zip(axs.ravel(), datasets):
    ax.plot(x, toa[50, :], marker="o", markersize=3, label="l1b")
    ax.plot(x, isrf[50, :], marker="o", markersize=3, label="ism")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(title)
    ax.legend()

plt.tight_layout()
plt.show()

fig2, axs2 = plt.subplots(2, 2, figsize=(12, 8))  # 2 filas, 2 columnas

datasets = [
    (l1b_toa0, ism_toa_isrf0, l1b_toa0_noeq, "toa0 vs isrf0 vs noeq"),
    (l1b_toa1, ism_toa_isrf1, l1b_toa1_noeq, "toa1 vs isrf1 vs noeq"),
    (l1b_toa2, ism_toa_isrf2, l1b_toa2_noeq, "toa2 vs isrf2 vs noeq"),
    (l1b_toa3, ism_toa_isrf3, l1b_toa3_noeq, "toa3 vs isrf3 vs noeq"),
]

for ax, (toa, isrf, noeq, title) in zip(axs2.ravel(), datasets):
    ax.plot(x, toa[50, :], marker="o", markersize=3, label="l1b")
    ax.plot(x, isrf[50, :], marker="o", markersize=3, label="ism")
    ax.plot(x, noeq[50, :], marker="x", markersize=3, label="l1b_noeq")  # el tercer array
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(title)
    ax.legend()

plt.tight_layout()
plt.show()
