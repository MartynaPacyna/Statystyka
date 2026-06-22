import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import statistics
import math

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