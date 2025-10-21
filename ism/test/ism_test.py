import matplotlib.pyplot as plt
import numpy as np

#read all necessary files
from common.io.writeToa import readToa
ism_toa0_isrf=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_isrf_VNIR-0.nc')
ism_toa1_isrf=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_isrf_VNIR-1.nc')
ism_toa2_isrf=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_isrf_VNIR-2.nc')
ism_toa3_isrf=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_isrf_VNIR-3.nc')

ism_toa0_isrf_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-0.nc')
ism_toa1_isrf_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-1.nc')
ism_toa2_isrf_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-2.nc')
ism_toa3_isrf_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_isrf_VNIR-3.nc')

ism_toa0_optical=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_optical_VNIR-0.nc')
ism_toa1_optical=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_optical_VNIR-1.nc')
ism_toa2_optical=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_optical_VNIR-2.nc')
ism_toa3_optical=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_optical_VNIR-3.nc')

ism_toa0_optical_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_optical_VNIR-0.nc')
ism_toa1_optical_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_optical_VNIR-1.nc')
ism_toa2_optical_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_optical_VNIR-2.nc')
ism_toa3_optical_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_optical_VNIR-3.nc')

ism_toa0=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_VNIR-0.nc')
ism_toa1=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_VNIR-1.nc')
ism_toa2=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_VNIR-2.nc')
ism_toa3=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\myoutputs','ism_toa_VNIR-3.nc')

ism_toa0_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_VNIR-0.nc')
ism_toa1_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_VNIR-1.nc')
ism_toa2_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_VNIR-2.nc')
ism_toa3_original=readToa(r'C:\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-ISM\output','ism_toa_VNIR-3.nc')

#Test 1
def diff_band(toa, toa_original):
    tol = 0.01
    diff= np.abs(toa_original - toa) / np.maximum(toa_original,1e-12) * 100
    mu = np.mean(diff)
    sigma = np.std(diff)
    threshold = mu + 3 * sigma
    ok = threshold < tol
    return threshold, ok
threshold0, ok0 = diff_band(ism_toa0_isrf , ism_toa0_isrf_original)
threshold1, ok1 = diff_band(ism_toa1_isrf , ism_toa1_isrf_original)
threshold2, ok2 = diff_band(ism_toa2_isrf , ism_toa2_isrf_original)
threshold3, ok3 = diff_band(ism_toa3_isrf , ism_toa3_isrf_original)
print("ISRF")
print("Band 0: threshold=", threshold0, ". below 0.01%?=", ok0)
print("Band 1: threshold=", threshold1, ". below 0.01%?=", ok1)
print("Band 2: threshold=", threshold2, ". below 0.01%?=", ok2)
print("Band 3: threshold=", threshold3, ". below 0.01%?=", ok3)
print("")

#Test 2
threshold0_o, ok0_o = diff_band(ism_toa0_optical , ism_toa0_optical_original)
threshold1_o, ok1_o = diff_band(ism_toa1_optical , ism_toa1_optical_original)
threshold2_o, ok2_o = diff_band(ism_toa2_optical , ism_toa2_optical_original)
threshold3_o, ok3_o = diff_band(ism_toa3_optical , ism_toa3_optical_original)
print("OPTICAL")
print("Band 0: threshold=", threshold0_o, ". below 0.01%?=", ok0_o)
print("Band 1: threshold=", threshold1_o, ". below 0.01%?=", ok1_o)
print("Band 2: threshold=", threshold2_o, ". below 0.01%?=", ok2_o)
print("Band 3: threshold=", threshold3_o, ". below 0.01%?=", ok3_o)
print("")

#Test 3
D = 0.150                           # [m] Telescope pupil diameter
f = 0.5262                          # [m] Focal length
Tr = 0.99                           # [-] Optical transmittance
rad2irrad_conversion_factor = Tr * (np.pi / 4) * (D/f)**2
print("rad2irrad Conversion Rate: ", rad2irrad_conversion_factor)
print("")

#SEGUNDA PARTE

#Test 1
threshold0_2, ok0_2 = diff_band(ism_toa0 , ism_toa0_original)
threshold1_2, ok1_2 = diff_band(ism_toa1 , ism_toa1_original)
threshold2_2, ok2_2 = diff_band(ism_toa2 , ism_toa2_original)
threshold3_2, ok3_2 = diff_band(ism_toa3 , ism_toa3_original)
print("OUTPUT")
print("Band 0: threshold=", threshold0_2, ". below 0.01%?=", ok0_2)
print("Band 1: threshold=", threshold1_2, ". below 0.01%?=", ok1_2)
print("Band 2: threshold=", threshold2_2, ". below 0.01%?=", ok2_2)
print("Band 3: threshold=", threshold3_2, ". below 0.01%?=", ok3_2)
print("")