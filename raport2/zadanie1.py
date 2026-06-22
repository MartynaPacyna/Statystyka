import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import statistics
import math
"""""
dane = []
#wczytywanie danych
with open("dane1.txt", "r", encoding="utf-8") as plik:
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
se = (odchylenie/np.sqrt(dlugosc))
print(se)
kwantyl = np.quantile(dane, 0.05)
print(f"kwantyl {kwantyl}")

#Hipoteza pierwsza, czyli obcinanie ogonów po lewej i po prawej stronie !=
#mi =! 1.5

for alpha in [0.01, 0.05, 0.10]:
    plt.figure(figsize=(10,10))
    print(f"--- DLA POZIOMU ISTOTNOŚCI alpha = {alpha} ---")
    # Przypadek A: mi != 1.5 (Dwustronny)
    mu = 1.5
    sigma = 0.2
    rozkład = stats.norm(0, 1)
    x = np.linspace(-4, 4, 500)
    y = rozkład.pdf(x) #gęstośc prawdopodbieństwa
    
    #wyznaczenie wartosci krytycznych z dwoch stron czyli alpha/2 i 1-alpha/2
    granica_lewa = rozkład.ppf(alpha/2)
    print(f'granica lewostronna {granica_lewa}')
    granica_prawa = rozkład.ppf(1 - alpha/2)
    print(f'granica prawostronna {granica_prawa}')
    
    plt.plot(x, y, label="rozkład normalny z parametrami N(0,1)")

    x_lewy = np.linspace(-4, granica_lewa, 100)
    plt.fill_between(x_lewy, rozkład.pdf(x_lewy), color='magenta', label='Obszar krytyczny lewostronny')

    x_prawy = np.linspace(granica_prawa, 4 , 100)
    plt.fill_between(x_prawy, rozkład.pdf(x_prawy), color='magenta', label='Obszar krytyczny prawostronny')
    
    plt.title(f"Hipoteza mi != 1.5 dla istotności alpha = {alpha}")
    plt.grid()
    plt.legend(loc='upper right', fontsize='small')
    plt.show()
    

    # Przypadek B: mi > 1.5 (Prawostronny)
for alpha in [0.01, 0.05, 0.10]:

    plt.figure(figsize=(10,10))
    print(f"--- DLA POZIOMU ISTOTNOŚCI alpha = {alpha} ---")
    mu = 1.5
    sigma = 0.2
    rozkład = stats.norm(0, 1)
    x = np.linspace(-4, 4, 500)
    y = rozkład.pdf(x) #gęstośc prawdopodbieństwa
    
    #wyznaczenie wartosci krytycznych z dwoch stron czyli 1 - alpha
    granica = rozkład.ppf(1 - alpha)
    print(f'granica prawostronna {granica}')
    
    plt.plot(x, y, label="rozkład normalny z parametrami N(0,1)")

    x_prawy = np.linspace(granica, 4 , 100)
    plt.fill_between(x_prawy, rozkład.pdf(x_prawy), color='magenta', label='Obszar krytyczny prawostronny')
    
    plt.title(f"Hipoteza mi > 1.5 dla istotności alpha = {alpha}")
    plt.grid()
    plt.legend(loc='upper right', fontsize='small')
    plt.show()

    # Przypadek C: mi < 1.5 (Lewostronny)
for alpha in [0.01, 0.05, 0.10]:
    plt.figure(figsize=(10,10))
    print(f"--- DLA POZIOMU ISTOTNOŚCI alpha = {alpha} ---")
    # Przypadek A: mi != 1.5 (Dwustronny)
    mu = 1.5
    sigma = 0.2
    rozkład = stats.norm(0, 1)
    x = np.linspace(-4, 4, 500)
    y = rozkład.pdf(x) #gęstośc prawdopodbieństwa
    
    #wyznaczenie wartosci krytycznych z dwoch stron czyli alpha
    granica_lewa = rozkład.ppf(alpha)
    print(f'granica lewostronna {granica_lewa}')
    
    plt.plot(x, y, label="rozkład normalny z parametrami N(0,1)")

    x_lewy = np.linspace(-4, granica_lewa, 100)
    plt.fill_between(x_lewy, rozkład.pdf(x_lewy), color='magenta', label='Obszar krytyczny lewostronny')
    
    plt.title(f"Hipoteza mi < 1.5 dla istotności alpha = {alpha}")
    plt.grid()
    plt.legend(loc='upper right', fontsize='small')
    plt.show()

sigma = 0.2
mu = 1.5
n = 1000
m = 100

poziomy_alpha = [0.01, 0.05, 0.10]
wyniki_pudełkowe = {}

rozkład_z = stats.norm(0, 1)

for alpha in poziomy_alpha:
    bledy_m = [] # Resetujemy listę dla każdego alpha

    granica_lewa = rozkład_z.ppf(alpha/2)
    granica_prawa = rozkład_z.ppf(1 - alpha/2)
    
    print(f"--- DLA POZIOMU ISTOTNOŚCI alpha = {alpha} ---")

    for _ in range(m):
        w_obszarze_krytycznym = 0

        for _ in range(n):
            X = np.random.normal(mu, sigma, n)

            dlugosc = len(X)
            srednia = statistics.mean(X)
            odchylenie = 0.2
            stat = (srednia - mu) / (odchylenie / np.sqrt(dlugosc))

            if stat <= granica_lewa or stat >= granica_prawa:
                w_obszarze_krytycznym += 1

        # POPRAWKA: Te trzy linijki MUSZĄ być wcięte pod pętlę 'm', żeby zebrać 100 wyników!
        przyblizenie_bledu = w_obszarze_krytycznym / n
        bledy_m.append(przyblizenie_bledu)
        
    wyniki_pudełkowe[alpha] = bledy_m

# Tworzymy tylko JEDNĄ figurę dla wykresu pudełkowego na samym końcu
plt.figure(figsize=(10, 6))
plt.boxplot([wyniki_pudełkowe[a] for a in poziomy_alpha], labels=[f"alpha = {a}" for a in poziomy_alpha])

# Dodanie linii teoretycznych wartości błędu I rodzaju dla porównania
for i, alpha in enumerate(poziomy_alpha, start=1):
    plt.axhline(y=alpha, color='red', linestyle='--', alpha=0.6, label='Wartość teoretyczna' if i == 1 else "")

plt.title("Symulacyjny błąd I rodzaju dla różnych poziomów istotności (M=100 powtórzeń)")
plt.ylabel("Otrzymany błąd I rodzaju")
plt.grid(True, axis='y', linestyle=':', alpha=0.6)
plt.legend()
plt.show()
"""
import numpy as np
import scipy.stats as stats
import statistics

alpha = 0.05
sigma = 0.2
n = 1000

mu_rozneod = [1.47, 1.48, 1.49, 1.51, 1.52, 1.53]
mu_wieksze = [1.51, 1.52, 1.53]
mu_mniejsze = [1.47, 1.48, 1.49]

rozkład_z = stats.norm(0, 1)

# --- 1. HIPOTEZA DWUSTRONNA (mu != 1.5) ---
print("--- TEST DWUSTRONNY ---")
granica_lewa_2s = rozkład_z.ppf(alpha / 2)
granica_prawa_2s = rozkład_z.ppf(1 - alpha / 2)

for mu in mu_rozneod:
    w_obszarze_akceptacji = 0
    for _ in range(n):
        X = np.random.normal(mu, sigma, n)
        srednia = statistics.mean(X)
        stat = (srednia - 1.5) / (sigma / np.sqrt(len(X)))
        
        # Błąd II rodzaju: statystyka wpada pomiędzy granice (brak odrzucenia H0)
        if stat > granica_lewa_2s and stat < granica_prawa_2s:
            w_obszarze_akceptacji += 1

    przyblizenie_bledu = w_obszarze_akceptacji / n
    print(f"mu = {mu}: Błąd II rodzaju = {przyblizenie_bledu}")


# --- 2. HIPOTEZA PRAWOSTRONNA (mu > 1.5) ---
print("\n--- TEST PRAWOSTRONNY ---")
granica_prawa_1s = rozkład_z.ppf(1 - alpha)

for mu in mu_wieksze:
    w_obszarze_akceptacji = 0
    for _ in range(n):
        X = np.random.normal(mu, sigma, n)
        srednia = statistics.mean(X)
        stat = (srednia - 1.5) / (sigma / np.sqrt(len(X)))
        
        # Błąd II rodzaju: statystyka nie wpada w prawy ogon krytyczny
        if stat <= granica_prawa_1s:
            w_obszarze_akceptacji += 1

    przyblizenie_bledu = w_obszarze_akceptacji / n
    print(f"mu = {mu}: Błąd II rodzaju = {przyblizenie_bledu}")


# --- 3. HIPOTEZA LEWOSTRONNA (mu < 1.5) ---
print("\n--- TEST LEWOSTRONNY ---")
granica_lewa_1s = rozkład_z.ppf(alpha)

for mu in mu_mniejsze:
    w_obszarze_akceptacji = 0
    for _ in range(n):
        X = np.random.normal(mu, sigma, n)
        srednia = statistics.mean(X)
        stat = (srednia - 1.5) / (sigma / np.sqrt(len(X)))
        
        # Błąd II rodzaju: statystyka nie wpada w lewy ogon krytyczny
        if stat >= granica_lewa_1s:
            w_obszarze_akceptacji += 1

    przyblizenie_bledu = w_obszarze_akceptacji / n
    print(f"mu = {mu}: Błąd II rodzaju = {przyblizenie_bledu}")