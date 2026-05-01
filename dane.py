import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.stats as stats

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'StudentsPerformance.csv')
df = pd.read_csv(file_path)

po_kursie = df[df['test preparation course'] == 'completed']['math score']
bez_kursu = df[df['test preparation course'] == 'none']['math score']


plt.xlim(0,100)
plt.hist(po_kursie, bins=25, label='Po kursie', color='#66b3ff', density=True)

mu, std = stats.norm.fit(po_kursie)
x = np.linspace(0, 100, 100)
plt.plot(x, stats.norm.pdf(x, mu, std), color='darkred', lw=2)

plt.title('Wyniki uczniów po kursie przygotowawczym')
plt.xlabel('Liczba uczniów')
plt.ylabel('Wyniki testu')
plt.legend()
plt.show()

plt.xlim(0,100)
plt.hist(bez_kursu, bins=25, label='Bez kursu', color='#ff9999', density=True)

mu, std = stats.norm.fit(bez_kursu)
x = np.linspace(0, 100, 100)
plt.plot(x, stats.norm.pdf(x, mu, std), color='darkred', lw=2)

plt.title('Wyniki uczniów bez kursu przygotowawczego')
plt.xlabel('Liczba uczniów')
plt.ylabel('Wyniki testu')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
bp = plt.boxplot([po_kursie, bez_kursu], 
                  labels=['Po kursie', 'Bez kursu'], 
                  showmeans=True, 
                  meanline=True, 
                  notch=True, 
                  patch_artist=True)

colors = ['#66b3ff', '#ff9999'] 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)


mean_po = po_kursie.mean()
mean_bez = bez_kursu.mean()

plt.axhline(mean_po, color='blue', linestyle=':', alpha=0.5, label=f'Średnia po kursie: {mean_po:.1f}')
plt.axhline(mean_bez, color='red', linestyle=':', alpha=0.5, label=f'Średnia bez kursu: {mean_bez:.1f}')

plt.title('Porównanie rozkładu wyników')
plt.ylabel('Wynik testu')
plt.legend()
plt.show()

print("Statystyki dla grupy PO KURSIE:")
print(po_kursie.describe())

print("\nStatystyki dla grupy BEZ KURSU:")
print(bez_kursu.describe())