import pandas
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.stats import skew


df = pandas.read_csv("StudentsPerformance.csv",sep=",")
df_completed = df[df["test preparation course"] == "completed"]
df_none = df[df["test preparation course"] == "none"]

wyniki_completed = df_completed["math score"].tolist()
wyniki_none = df_none["math score"].tolist()



def srednia_ucinana(dane,k):
    dane_sort = sorted(dane)
    n= len(dane)
    if k == 0:
        return sum(dane)/n

    suma = sum(dane_sort[k:-k])
    wynik = suma/(n-2*k)
    return wynik

def srednia_winsorowska(dane,k):
    dane_sort = sorted(dane)
    n= len(dane)
    if k == 0:
        return sum(dane)/n

    sum_p = dane_sort[k]*k
    sum_k = dane_sort[-k-1]*k

    suma = sum(dane_sort[k:-k]) + sum_p + sum_k
    wynik = suma/n
    return wynik

def wykresy(dane):
    max_k = len(dane) 
    x = range(0, len(dane)//2)
    srednie_ucinane = [srednia_ucinana(dane, k) for k in x]

    sr = np.mean(dane)
    med = np.median(dane)

    #plt.figure(figsize = (10,4))
    #plt.subplot(1, 2, 1)

    plt.plot(x, srednie_ucinane, color='#F4A261',label = 'średnia ucinana')
    #plt.plot(x,[sr]*len(x), color ='pink',label = 'srednia arytmetyczna')
    #plt.plot(x, [med]*len(x),color='orange',label = 'mediana')
    #plt.xlabel("k")
    #plt.ylabel("srednia")
    #plt.title("srednia ucinana od k")
    #plt.legend()

    srednie_winsorowskie = [srednia_winsorowska(dane, k) for k in x]
   # plt.subplot(1, 2, 2)
    plt.plot(x, srednie_winsorowskie, color='#E76F8A',label = 'średnia winsorowska')
    plt.plot(x,[sr]*len(x), color ='#C77DFF',label = 'średnia arytmetyczna')
    plt.plot(x, [med]*len(x),color='#9D8DF1',label = 'mediana')
    plt.xlabel("k")
    plt.ylabel("średnia")
    plt.title("średnia ucinana i winsorowska jako funkcje parametru k")

    #plt.grid(True)
    plt.legend()

    #plt.tight_layout()
    plt.show()

def K1(dane):
    dane = np.array(dane, dtype=float)
    n = len(dane) 
    x_sr = np.mean(dane) 
    m2 = np.sum((dane - x_sr)**2) / n
    m4 = np.sum((dane - x_sr)**4) / n
    K1 = m4 / (m2**2)
    return K1

def K(dane):
    dane = np.array(dane, dtype=float)
    n = len(dane)
    x_sr = np.mean(dane) 
    m2 = np.sum((dane - x_sr)**2) / n
    m4 = np.sum((dane - x_sr)**4) / n
    K1 = m4 / (m2**2)
    K = ((n - 1) / ((n - 2) * (n - 3))) * ((n + 1) * K1 - 3 * (n - 1)) + 3
    
    return K
def O_P(x):
    x = np.array(x)
    return np.mean(np.abs(x - np.mean(x)))

   
print("srednia arytmetyczna completed: ", np.mean(wyniki_completed))
print("srednia ucinana completed, k=36",srednia_ucinana(wyniki_completed,36))
print("srednia win completed, k=36",srednia_winsorowska(wyniki_completed,36))
print("")
print("srednia arytmetyczna none: ", np.mean(wyniki_none))
print("srednia ucinana none, k=64",srednia_ucinana(wyniki_none,64))
print("srednia win none, k=64",srednia_winsorowska(wyniki_none,64))
print("")
print("srednia none",np.mean(wyniki_none)-np.median(wyniki_none))
print("srednia comp",np.mean(wyniki_completed)-np.median(wyniki_completed))
print("")
print("mediana none",np.median(wyniki_none))
print("mediana comp",np.median(wyniki_completed))
print("")
print("Q1 none",np.quantile(wyniki_none, 0.25))
print("Q1 comp",np.quantile(wyniki_completed, 0.25))
print("")
print("Q3 none",np.quantile(wyniki_none, 0.75))
print("Q3 comp",np.quantile(wyniki_completed, 0.75))
print("")
print("K1 none",K1(wyniki_none))
print("K1 comp",K1(wyniki_completed))
print("")
print("K none",K(wyniki_none))
print("K comp",K(wyniki_completed))
print("")
print("Var none",np.var(wyniki_none, ddof=1))
print("Var comp",np.var(wyniki_completed, ddof=1))
print("")
print("odchylenie standardowe none",np.sqrt(np.var(wyniki_none, ddof=1)))
print("odchylenie standardowe comp",np.sqrt(np.var(wyniki_completed, ddof=1)))
print("")
print("odchylenie przecietne od wartosci sredniej none",O_P(wyniki_none))
print("odchylenie przecietne od wartosci sredniej comp",O_P(wyniki_completed))
print("")
print("skosnosc none",skew(wyniki_none, bias=False))
print("skosnosc comp",skew(wyniki_completed, bias=False))


wykresy(wyniki_completed)
wykresy(wyniki_none)


