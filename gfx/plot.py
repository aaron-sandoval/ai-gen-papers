# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GDP(filename):
    # Load data from CSV file
    data = pd.read_csv(filename)

    # Set up the figure and axes
    plt.figure(figsize=(10, 6))
    ax = plt.axes()

    # Set the color scheme
    sns.set_palette("Paired")

    # Plot the data
    plt.plot(data['China'], label='China')
    plt.plot(data['USA'], label='USA')
    plt.plot(data['Russia'], label='Russia')

    # Set the title and axis labels
    plt.title('GDP Trends from 1980 to 2020 (in USD)')
    plt.xlabel('Year')
    plt.ylabel('GDP (in USD)')

    # Set the tick labels
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(range(1980, 2021, 5))
    ax.ticklabel_format(style='plain', axis='y')

    # Add a legend
    plt.legend()

    # Set the grid and axis limits
    plt.grid(True)
    plt.xlim(0, len(data) - 1)
    plt.ylim(0, max(data.max()))

    # Save the plot
    plt.savefig('GDP_plot.png', dpi=300, bbox_inches='tight')

    # Show the plot
    plt.show()