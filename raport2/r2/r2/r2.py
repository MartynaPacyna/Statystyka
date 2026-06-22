'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# --- DANE Z ZADANIA (ZMIENIONO NA ALPHA = 0.10) ---
alpha = 0.10
df = 1000  # n = 1000 stopni swobody
chi2_stat = 1112.579914

# Definicja osi X dla wykresów
x = np.linspace(800, 1250, 1000)
y = stats.chi2.pdf(x, df)

# Wyznaczenie dokładnych wartości krytycznych dla alpha = 0.10
c_dwustronny_lewy = stats.chi2.ppf(alpha / 2, df)  # ~927.59
c_dwustronny_prawy = stats.chi2.ppf(1 - alpha / 2, df)  # ~1074.68
c_jednostronny_prawy = stats.chi2.ppf(1 - alpha, df)  # ~1057.72
c_jednostronny_lewy = stats.chi2.ppf(alpha, df)  # ~943.13

# Pobranie maksymalnej wartości y do pozycjonowania etykiet tekstowych
max_y = max(y)

# --- WYKRES 1: DWUSTRONNY (H1: sigma^2 != 1.5) ---
  # Zapewnia osobną przestrzeń dla wykresu
plt.plot(x, y, "g-", label="Gęstość rozkładu $\chi^2$")

x_left = np.linspace(800, c_dwustronny_lewy, 100)
plt.fill_between(
    x_left,
    stats.chi2.pdf(x_left, df),
    color="pink",
    alpha=0.5,
    label="Obszar krytyczny",
)
x_right = np.linspace(c_dwustronny_prawy, 1250, 100)
plt.fill_between(x_right, stats.chi2.pdf(x_right, df), color="pink", alpha=0.5)

plt.axvline(c_dwustronny_lewy, color="red", linestyle=":", alpha=0.7)
plt.axvline(c_dwustronny_prawy, color="red", linestyle=":", alpha=0.7)
plt.axvline(chi2_stat, color="orange", linestyle=":")

plt.text(
    chi2_stat + 5,
    max_y * 0.4,
    f"$\chi^2_{{obl}} = {chi2_stat:.2f}$",
    color="darkorange",
    weight="bold",
    ha="left",
    rotation=90,
)

plt.title("$H_1: \sigma^2 \\neq 1.5$")
plt.xticks(
    [c_dwustronny_lewy, df, c_dwustronny_prawy],
    [f"{c_dwustronny_lewy:.2f}", f"n={df}", f"{c_dwustronny_prawy:.2f}"],
    rotation=45,
    ha="right",
)
plt.legend()
plt.tight_layout()
plt.show()


# --- WYKRES 2: PRAWOSTRONNY (H1: sigma^2 > 1.5) ---
 # Zapewnia osobną przestrzeń dla wykresu
plt.plot(x, y, "g-", label="Gęstość rozkładu $\chi^2$")

x_right_only = np.linspace(c_jednostronny_prawy, 1250, 100)
plt.fill_between(
    x_right_only,
    stats.chi2.pdf(x_right_only, df),
    color="pink",
    alpha=0.5,
    label="Obszar krytyczny",
)

plt.axvline(c_jednostronny_prawy, color="red", linestyle=":", alpha=0.7)
plt.axvline(chi2_stat, color="orange", linestyle=":")

plt.text(
    chi2_stat + 5,
    max_y * 0.4,
    f"$\chi^2_{{obl}} = {chi2_stat:.2f}$",
    color="darkorange",
    weight="bold",
    ha="left",
    rotation=90,
)

plt.title("$H_1: \sigma^2 > 1.5$")
plt.xticks(
    [df, c_jednostronny_prawy],
    [f"n={df}", f"{c_jednostronny_prawy:.2f}"],
    rotation=45,
    ha="right",
)
plt.legend()
plt.tight_layout()
plt.show()


# --- WYKRES 3: LEWOSTRONNY (H1: sigma^2 < 1.5) ---
 # Zapewnia osobną przestrzeń dla wykresu
plt.plot(x, y, "g-", label="Gęstość rozkładu $\chi^2$")

x_left_only = np.linspace(800, c_jednostronny_lewy, 100)
plt.fill_between(
    x_left_only,
    stats.chi2.pdf(x_left_only, df),
    color="pink",
    alpha=0.5,
    label="Obszar krytyczny",
)

plt.axvline(c_jednostronny_lewy, color="red", linestyle=":", alpha=0.7)
plt.axvline(chi2_stat, color="orange", linestyle=":")

plt.text(
    chi2_stat + 5,
    max_y * 0.4,
    f"$\chi^2_{{obl}} = {chi2_stat:.2f}$",
    color="darkorange",
    weight="bold",
    ha="left",
    rotation=90,
)

plt.title("$H_1: \sigma^2 < 1.5$")
plt.xticks(
    [c_jednostronny_lewy, df],
    [f"{c_jednostronny_lewy:.2f}", f"n={df}"],
    rotation=45,
    ha="right",
)
plt.legend()
plt.tight_layout()
plt.show()
'''
'''
import numpy as np

try:
    data = np.loadtxt("dane2.txt")
except FileNotFoundError:
    exit()

mu_theoretical = 0.2
sigma2_zero = 1.5

chi2_stat = np.sum((data - mu_theoretical) ** 2) / sigma2_zero

print(f"{chi2_stat}")
'''


'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

n = 1000
N = 1000
M = 100
alphas = [0.01, 0.05, 0.10]

mu_true = 1.5
sigma_true = 0.2
sigma0_sq = sigma_true ** 2

results = {
    'dwustronny': {alpha: [] for alpha in alphas},
    'prawostronny': {alpha: [] for alpha in alphas},
    'lewostronny': {alpha: [] for alpha in alphas}
}



for m in range(M):
    for alpha in alphas:
        crit_left_2st = stats.chi2.ppf(alpha/2, n)
        crit_right_2st = stats.chi2.ppf(1-alpha/2, n)
        crit_right_1st = stats.chi2.ppf(1-alpha, n)
        crit_left_1st = stats.chi2.ppf(alpha, n)
        
        rejections_2st = 0
        rejections_right = 0
        rejections_left = 0
        
        for _ in range(N):
            sample = np.random.normal(loc=mu_true, scale=sigma_true, size=n)
            
            chi2_stat = np.sum((sample - mu_true) ** 2) / sigma0_sq
            
            if chi2_stat <= crit_left_2st or chi2_stat >= crit_right_2st:
                rejections_2st += 1
            if chi2_stat >= crit_right_1st:
                rejections_right += 1
            if chi2_stat <= crit_left_1st:
                rejections_left += 1
                
        results['dwustronny'][alpha].append(rejections_2st / N)
        results['prawostronny'][alpha].append(rejections_right / N)
        results['lewostronny'][alpha].append(rejections_left / N)

tests = ['dwustronny', 'prawostronny', 'lewostronny']
titles = ['$H_1: \\sigma^2 \\neq 0.04$', 
          '$H_1: \\sigma^2 > 0.04$', 
          '$H_1: \\sigma^2 < 0.04$']

for i, test in enumerate(tests):
    plt.figure() 
    data_to_plot = [results[test][alpha] for alpha in alphas]
    
    plt.boxplot(data_to_plot, tick_labels=[f'$\\alpha$={a}' for a in alphas])
    plt.title(titles[i])
    plt.xlabel('teoretyczny poziom istotności')
    plt.ylabel('empiryczny błąd I rodzaju')
    plt.ylim(-0.02, 0.15) 
    
    plt.tight_layout()

plt.show()
'''



'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

n = 1000
N = 1000
M = 100
alphas = [0.01, 0.05, 0.10]

# Parametry dla testu wariancji
mu_true = 0.2
sigma0_sq = 1.5
sigma_true = np.sqrt(sigma0_sq)  # Pierwiastek z 1.5, żeby wariancja wynosiła 1.5

results = {
    'dwustronny': {alpha: [] for alpha in alphas},
    'prawostronny': {alpha: [] for alpha in alphas},
    'lewostronny': {alpha: [] for alpha in alphas}
}

np.random.seed(42)

for m in range(M):
    for alpha in alphas:
        crit_left_2st = stats.chi2.ppf(alpha/2, n)
        crit_right_2st = stats.chi2.ppf(1-alpha/2, n)
        crit_right_1st = stats.chi2.ppf(1-alpha, n)
        crit_left_1st = stats.chi2.ppf(alpha, n)
        
        rejections_2st = 0
        rejections_right = 0
        rejections_left = 0
        
        for _ in range(N):
            sample = np.random.normal(loc=mu_true, scale=sigma_true, size=n)
            
            # Statystyka testowa dla znanej średniej mu
            chi2_stat = np.sum((sample - mu_true) ** 2) / sigma0_sq
            
            if chi2_stat <= crit_left_2st or chi2_stat >= crit_right_2st:
                rejections_2st += 1
            if chi2_stat >= crit_right_1st:
                rejections_right += 1
            if chi2_stat <= crit_left_1st:
                rejections_left += 1
                
        results['dwustronny'][alpha].append(rejections_2st / N)
        results['prawostronny'][alpha].append(rejections_right / N)
        results['lewostronny'][alpha].append(rejections_left / N)

# --- TWORZENIE TRZECH WYKRESÓW OBOK SIEBIE Z RÓŻOWĄ LINIĄ ---

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

tests = ['dwustronny', 'prawostronny', 'lewostronny']
test_labels = ['$H_1: \\sigma^2 \\neq 1.5$', 
               '$H_1: \\sigma^2 > 1.5$', 
               '$H_1: \\sigma^2 < 1.5$']

for idx, alpha in enumerate(alphas):
    data_to_plot = [results[test][alpha] for test in tests]
    
    # Klasyczny boxplot bez wypełnienia kolorem
    axes[idx].boxplot(data_to_plot, tick_labels=test_labels)
    
    # Różowa linia ciągła dla teoretycznej wartości alfa
    axes[idx].axhline(y=alpha, color='pink', linestyle='-', linewidth=2, label=f'wartość teoretyczna $\\alpha = {alpha}$')
    
    axes[idx].set_title(f'Poziom istotności $\\alpha = {alpha}$')
    axes[idx].set_ylim(-0.02, 0.15)
    axes[idx].legend(loc='upper right')
    
    if idx == 0:
        axes[idx].set_ylabel('Empiryczny błąd I rodzaju')

plt.tight_layout()
plt.show()

'''

import numpy as np
import scipy.stats as stats
import pandas as pd

# Ustawienia symulacji
n = 1000
N = 1000
alpha = 0.05
mu_true = 0.2
sigma0_sq = 1.5

# Wartości wariancji dla hipotez alternatywnych
alternatives = {
    'dwustronny': [1.47, 1.48, 1.49, 1.51, 1.52, 1.53],
    'prawostronny': [1.51, 1.52, 1.53],
    'lewostronny': [1.47, 1.48, 1.49]
}

# Granice krytyczne (stałe dla ustalonego alpha i n)
crit_left_2st = stats.chi2.ppf(alpha/2, n)
crit_right_2st = stats.chi2.ppf(1-alpha/2, n)
crit_right_1st = stats.chi2.ppf(1-alpha, n)
crit_left_1st = stats.chi2.ppf(alpha, n)

results_table = []

# Symulacja
for test_type, sigmas in alternatives.items():
    for sigma_alt_sq in sigmas:
        sigma_alt = np.sqrt(sigma_alt_sq)
        non_rejections = 0
        
        for _ in range(N):
            sample = np.random.normal(loc=mu_true, scale=sigma_alt, size=n)
            chi2_stat = np.sum((sample - mu_true) ** 2) / sigma0_sq
            
            is_rejected = False
            if test_type == 'dwustronny':
                is_rejected = (chi2_stat <= crit_left_2st or chi2_stat >= crit_right_2st)
            elif test_type == 'prawostronny':
                is_rejected = (chi2_stat >= crit_right_1st)
            elif test_type == 'lewostronny':
                is_rejected = (chi2_stat <= crit_left_1st)
            
            if not is_rejected:
                non_rejections += 1
                
        beta = non_rejections / N
        moc_testu = 1 - beta
        
        results_table.append({
            'Test': test_type, 
            'Sigma^2_alt': sigma_alt_sq, 
            'Błąd II rodzaju (beta)': beta,
            'Moc testu': moc_testu
        })

# Wyświetlenie tabeli
df = pd.DataFrame(results_table)

# Ustawienia wyświetlania dla czytelności
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("--- BŁĄD II RODZAJU (BETA) ---")
print(df.pivot(index='Sigma^2_alt', columns='Test', values='Błąd II rodzaju (beta)'))

print("\n--- MOC TESTU ---")
print(df.pivot(index='Sigma^2_alt', columns='Test', values='Moc testu'))
