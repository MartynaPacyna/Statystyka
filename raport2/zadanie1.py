import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import statistics
import math

dane = []
#wczytywanie danych
with open("raport2\dane1.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        tekst = linia.strip()
        if not tekst:
            continue
        try:
            liczba = float(tekst)
            dane.append(liczba)
        except ValueError:
            continue
sigma = 0.2
alpha = 0.05

#Hipoteza zerowa
mi = 1.5 
dlugosc = len(dane)
print(f'Dlugosc porby: {dlugosc}')
srednia = statistics.mean(dane)
print(f'Średnia porby: {srednia}')
mediana = np.median(dane)
print(f'Mediana porby: {mediana}')
odchylenie = 0.2
wariancja = np.var(dane)
print(f'Wariancja porby: {wariancja}')
speed_test_stdev = 0.2
print(f'STEDV porby: {speed_test_stdev}')

#STATYSTYKA TESTOWA ma wzor
stat = (srednia - mi)/(odchylenie/np.sqrt(dlugosc))
print(stat)
"""""
z_score = (srednia - mi) / (speed_test_stdev/math.sqrt(dlugosc))
print(f'Z: {z_score}')
#Hipoteza pierwsza, czyli obcinanie ogonów po lewej i po prawej stronie
#mi =! 1.5
for alpha in [0.01, 0.05, 0.10]:
    print(f"--- DLA POZIOMU ISTOTNOŚCI alpha = {alpha} ---")
    # Przypadek A: mi != 1.5 (Dwustronny)
    z_crit_two = stats.norm.ppf(1 - alpha/2)
    p_two = 2 * (1 - stats.norm.cdf(abs(z_score)))
    print(f"Hipoteza mi != 1.5: Obszar krytyczny = (-inf, {-z_crit_two:.4f}) U ({z_crit_two:.4f}, +inf) | p-wartość = {p_two:.6f}")
    
    # Przypadek B: mi > 1.5 (Prawostronny)
    z_crit_right = stats.norm.ppf(1 - alpha)
    p_right = 1 - stats.norm.cdf(z_score)
    print(f"Hipoteza mi > 1.5:  Obszar krytyczny = ({z_crit_right:.4f}, +inf) | p-wartość = {p_right:.6f}")
    
    # Przypadek C: mi < 1.5 (Lewostronny)
    z_crit_left = stats.norm.ppf(alpha)
    p_left = stats.norm.cdf(z_score)
    print(f"Hipoteza mi < 1.5:  Obszar krytyczny = (-inf, {z_crit_left:.4f}) | p-wartość = {p_left:.6f}")

x = np.linspace(-8, 4, 1000)
y = stats.norm.pdf(x, 0, 1)
z_crit_5 = stats.norm.ppf(1 - 0.1/2)
z_crit_r5 = stats.norm.ppf(1 - 0.1)

# Wykres 1: Dwustronny
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', label='Gęstość N(0,1)')
plt.fill_between(x, y, where=(x > z_crit_5) | (x < -z_crit_5), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(z_score, color='green', linestyle='--', label=f'Nasze Z = {z_score:.2f}')
plt.title('Test dwustronny (mi != 1.5) dla alpha=0.1')
plt.legend()
plt.grid(True)

# Wykres 2: Prawostronny
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', label='Gęstość N(0,1)')
plt.fill_between(x, y, where=(x > z_crit_r5), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(z_score, color='green', linestyle='--', label=f'Nasze Z = {z_score:.2f}')
plt.title('Test prawostronny (mi > 1.5) dla alpha=0.05')
plt.legend()
plt.grid(True)

# Wykres 3: Lewostronny
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', label='Gęstość N(0,1)')
plt.fill_between(x, y, where=(x < -z_crit_r5), color='red', alpha=0.5, label='Obszar krytyczny')
plt.axvline(z_score, color='green', linestyle='--', label=f'Nasze Z = {z_score:.2f}')
plt.title('Test lewostronny (mi < 1.5) dla alpha=0.05')
plt.legend()
plt.grid(True)

plt.show()
"""