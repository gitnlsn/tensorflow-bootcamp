import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import os

# Create output directory
output_dir = 'output_plots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("=== Basic Line Plot ===")
x = np.arange(0, 10)
y = x**2
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig(f'{output_dir}/01_basic_line_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '01_basic_line_plot.png'")

print("\n=== Multiple Plots ===")
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r-', label='x²')
plt.plot(x, x*2, 'b--', label='2x')
plt.title("Multiple Lines")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y, 'go')
plt.title("Scatter Points")

plt.tight_layout()
plt.savefig(f'{output_dir}/02_multiple_plots.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '02_multiple_plots.png'")

print("\n=== Styling and Markers ===")
x_data = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x_data)
y2 = np.cos(x_data)

plt.figure(figsize=(8, 6))
plt.plot(x_data, y1, 'r-', linewidth=2, label='sin(x)')
plt.plot(x_data, y2, 'b--', linewidth=2, label='cos(x)')
plt.title("Trigonometric Functions", fontsize=16)
plt.xlabel("X (radians)", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(f'{output_dir}/03_styling_markers.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '03_styling_markers.png'")

print("\n=== Bar Chart ===")
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(value), ha='center', va='bottom')

plt.savefig(f'{output_dir}/04_bar_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '04_bar_chart.png'")

print("\n=== Histogram ===")
np.random.seed(42)
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
plt.title("Histogram - Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axvline(data.mean(), color='red', linestyle='--', label=f'Mean: {data.mean():.2f}')
plt.legend()
plt.savefig(f'{output_dir}/05_histogram.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '05_histogram.png'")

print("\n=== Scatter Plot ===")
np.random.seed(123)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100)

plt.figure(figsize=(8, 6))
plt.scatter(x_scatter, y_scatter, alpha=0.6, c='purple')
plt.title("Scatter Plot")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")

z = np.polyfit(x_scatter, y_scatter, 1)
p = np.poly1d(z)
plt.plot(x_scatter, p(x_scatter), "r--", alpha=0.8, label=f'Trend line: y={z[0]:.2f}x+{z[1]:.2f}')
plt.legend()
plt.savefig(f'{output_dir}/06_scatter_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '06_scatter_plot.png'")

print("\n=== Heatmap ===")
data_matrix = np.random.randint(0, 100, (10, 10))

plt.figure(figsize=(8, 6))
im = plt.imshow(data_matrix, cmap='viridis', interpolation='nearest')
plt.title("Heatmap Example")
plt.colorbar(im)
plt.savefig(f'{output_dir}/07_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '07_heatmap.png'")

print("\n=== Subplots with different chart types ===")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

x_sub = np.linspace(0, 10, 100)
y_sub = np.sin(x_sub)

ax1.plot(x_sub, y_sub)
ax1.set_title("Line Plot")
ax1.grid(True)

ax2.scatter(np.random.randn(50), np.random.randn(50))
ax2.set_title("Scatter Plot")

ax3.bar(['Q1', 'Q2', 'Q3', 'Q4'], [20, 35, 30, 25])
ax3.set_title("Bar Chart")

ax4.pie([30, 25, 20, 25], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
ax4.set_title("Pie Chart")

plt.tight_layout()
plt.savefig(f'{output_dir}/08_subplots.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '08_subplots.png'")

print("\n=== Advanced Customization ===")
x_custom = np.linspace(0, 4*np.pi, 200)
y_custom = np.exp(-x_custom/8) * np.sin(x_custom)

plt.figure(figsize=(10, 6))
plt.plot(x_custom, y_custom, linewidth=3, color='darkblue')
plt.fill_between(x_custom, y_custom, alpha=0.3, color='lightblue')
plt.title("Damped Oscillation", fontsize=18, fontweight='bold')
plt.xlabel("Time", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.grid(True, alpha=0.5)
plt.xlim(0, 4*np.pi)
plt.savefig(f'{output_dir}/09_advanced_customization.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '09_advanced_customization.png'")

print("\n=== Color Maps and 3D-like effect ===")
x_3d = np.linspace(-5, 5, 50)
y_3d = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_3d, y_3d)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, levels=20, cmap='plasma')
plt.colorbar(contour)
plt.title("Contour Plot - 3D Surface Projection")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig(f'{output_dir}/10_contour_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Gráfico salvo como '10_contour_plot.png'")

print(f"\n🎯 Todos os gráficos foram salvos na pasta '{output_dir}/'")
print("📊 Total de 10 gráficos gerados com sucesso!")
print("\n📋 Lista de arquivos gerados:")
for i, name in enumerate([
    "01_basic_line_plot.png",
    "02_multiple_plots.png", 
    "03_styling_markers.png",
    "04_bar_chart.png",
    "05_histogram.png",
    "06_scatter_plot.png",
    "07_heatmap.png", 
    "08_subplots.png",
    "09_advanced_customization.png",
    "10_contour_plot.png"
], 1):
    print(f"   {i:2d}. {name}")
