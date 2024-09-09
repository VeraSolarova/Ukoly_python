"""vytvořte soubor 11_graf.py

vytvořte sloupcový graf (bar chart) pomocí matplotlib:

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
}

ukázku máte v test_bar_chart.py
je možné že data budete muset upravit nebo použit nějaké dict metody,
aby jste dostali vhodné vstupy pro graf"""

import matplotlib.pyplot as plt
import numpy as np

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
}

mesta = []
obyvatele = []

for mesto, obyvatel in data.items():
    mesta.append(mesto)
    obyvatele.append(obyvatel)

print(mesta)
print(obyvatel)



plt.style.use('_mpl-gallery')


x = 0.5 + np.arange(4)
y = obyvatele

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 4), xticks=np.arange(1, 5),
       ylim=(0, 1_500_000), yticks=np.arange(1, 1_500_000, 200_000))

plt.show()
