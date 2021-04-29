import numpy as np
import matplotlib.pyplot as plt

# a)
weight,height = np.genfromtxt("Groesse_Gewicht.txt",unpack=True)

plt.subplots(6,2,sharex=True)

bins = [5,10,15,20,30,50]

for i in range(3*2):
    plt.subplot(6,2,2*i+1)
    plt.ylabel('count')
    if i==len(bins)-1: plt.xlabel('height')
    plt.hist(height,bins=bins[i],label=f'bins={bins[i]}')
    plt.legend()

    plt.subplot(6,2,2*i+2)
    if i==len(bins)-1: plt.xlabel('weight')
    plt.hist(weight,bins=bins[i],label=f'bins={bins[i]}',color='orange')
    plt.legend()

plt.tight_layout()

# 10 bins vernünftig? Weil es sonst zu fein aufgelöst ist für ein recht kleines dataset

# b)
# wenn viel mehr Personen aufgenommen werden ist es näher an einer Normalverteilung
# es könnte sinnvoll sein dann mehr bins zu nehmen
# sinnvolle minimale bin-breite:
# größe: 0.05
# gewicht: 1.0
# bin mitten:
# größe: 0.05
# gewicht 1.0

# c)
rg = np.random.default_rng(42)
numbers = rg.integers(1,101,10**5)
log_nums = np.log(numbers)

plt.subplots(3,2,sharex=True)

for i in range(3*2):
    plt.subplot(3,2,i+1)
    plt.ylabel('count')
    plt.xlabel('log(x)')
    plt.hist(log_nums,bins=bins[i],label=f'bins={bins[i]}')
    plt.legend()

plt.tight_layout()
plt.show()

# bei vielen Bins entstehen lücken