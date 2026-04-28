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

x = np.linspace(0, 100, 100)
mu_po, std_po = stats.norm.fit(po_kursie)
plt.plot(x, stats.norm.pdf(x, mu_po, std_po), color='darkred', lw=2)

plt.xlim(0,100)
plt.hist(po_kursie, bins=25, label='Po kursie', color='pink', density=True)
plt.title('Wyniki uczniów po kursu przygotowawczego')
plt.legend()
plt.show()

mu_bez, std_bez = stats.norm.fit(bez_kursu)
plt.plot(x, stats.norm.pdf(x, mu_bez, std_bez), color='darkred', lw=2)
plt.xlim(0,100)
plt.hist(bez_kursu, bins=25, label='Bez kursu', color='pink', density=True)
plt.title('Wyniki uczniów bez kursu przygotowawczego')
plt.legend()
plt.show()

plt.boxplot([bez_kursu, po_kursie], labels=['Bez kursu', 'Po kursie'], showmeans=True, notch=True)

plt.title('Porównanie rozkładu wyników')
plt.ylabel('Wynik testu')
plt.show()

print("Statystyki dla grupy PO KURSIE:")
print(po_kursie.describe())

print("\nStatystyki dla grupy BEZ KURSU:")
print(bez_kursu.describe())