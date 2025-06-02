import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import sklearn as skl

# Primeira parte
np.random.seed(42)
arr = np.random.randint(501, size=(100, 5))
print("Array aleatório:", arr)

# Segunda parte
fig, ax = plt.subplots()
cax = ax.imshow(arr, vmin=0, vmax=500, cmap='coolwarm')
ax.set_title('Array de números aleatórios com colorbar vertical')
cbar = fig.colorbar(cax,
                    ticks=[0, 250, 500],
                    format=mticker.FixedFormatter(['< 0', '250', '> 500']),
                    extend='both'
                    )
labels = cbar.ax.get_yticklabels()
labels[0].set_verticalalignment('top')
labels[-1].set_verticalalignment('bottom')
plt.savefig('src/libraries-review/exercises/array_visualization.png', dpi=300, bbox_inches='tight')
plt.close()
print("Imagem salva como 'array_visualization.png'")

# Terceira parte
data = pd.DataFrame(data=arr, columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(data.head())

# Quarta parte
data.rename(columns={"col1": "f1", "col2": "f2", "col3": "f3", "col4": "f4", "col5": "f5"}, inplace=True)

print(data.head())
