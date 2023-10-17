###
Box.csv contained columns of 'Sample_number', 'Glucose % loss', 'Sucrose % loss', 'L-arginine % loss' etc.
###

import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
csv_file = 'box.csv'  # Replace with your CSV file's path
data = pd.read_csv(csv_file)

# Define colors for box plots
num_boxplots = len(data.columns)
colors = ['#F39C12' if i < 4 else '#5DADE2' for i in range(num_boxplots)]

# Create a box plot with colored boxes
plt.figure(figsize=(16,12))  # Optional: Adjust figure size
box_plot = plt.boxplot(data.values, labels=data.columns, patch_artist=True, widths = 0.7)

# Assign colors to boxes
for box, color in zip(box_plot['boxes'], colors):
    box.set_facecolor(color)

# Change the color of the lines inside each box to black
for line in box_plot['medians']:
    line.set_color('black')
for line in box_plot['whiskers']:
    line.set_color('black')

# Annotate median values
for i, line in enumerate(box_plot['medians']):
    # Get the median value
    median_value = line.get_ydata()[0]

    # Annotate the median value on the plot
    plt.annotate(f'{median_value:.2f}', (i+1, median_value), xytext=(0, 10), textcoords='offset points',
                 fontsize=10, ha='center',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('Compound', fontsize=16)
plt.ylabel('Percent change', fontsize=16)
plt.title('Percent change in free amino acid, free sugar, and total amino acid content after heat treatment', fontweight='bold', fontsize=18)
plt.xticks(rotation=60, fontweight="bold")  # Rotates X-Axis Ticks by 45-degrees
plt.tight_layout()  # Optional: Adjust layout
plt.show()
