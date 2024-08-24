import pandas as pd
import matplotlib.pyplot as plt

def plot_GDP(data_file):
    # Load the data from the file
    data = pd.read_csv(data_file)

    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the data as line graphs
    data.plot(ax=ax, linewidth=2)

    # Set the title and axis labels
    ax.set_title('GDP Growth Over Time', fontsize=16)
    ax.set_xlabel('Time', fontsize=14)
    ax.set_ylabel('GDP', fontsize=14)

    # Set the legend properties
    ax.legend(loc='upper left', fontsize=12)

    # Set the grid lines
    ax.grid(linestyle='--', alpha=0.5)

    # Adjust the spacing between subplots
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.5, wspace=0.5)

    # Show the plot
    plt.show()