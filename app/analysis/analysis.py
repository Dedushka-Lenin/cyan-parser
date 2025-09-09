import sys
import os

import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

import seaborn as sns


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.repo.offerRepo import OfferRepo



offerRepo = OfferRepo()

data = offerRepo.get()

df = pd.DataFrame(data)
print(df.describe())


plt.figure(figsize=(24, 6))

plt.subplot(1, 3, 1)
sns.histplot(df['price'], bins=50, kde=True, color='skyblue')
plt.title('Распределение цены')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.subplot(1, 3, 2)
sns.histplot(df['price_per_meter'], bins=50, kde=True, color='salmon')
plt.title('Распределение цены за метр')
plt.xlabel('Цена за метр')
plt.ylabel('Частота')

plt.subplot(1, 3, 3)
sns.histplot(df['square'], bins=100, kde=True)
plt.title('Распределение площади')
plt.xlabel('Площадь (м²)')
plt.ylabel('Частота')

plt.tight_layout()
plt.show()