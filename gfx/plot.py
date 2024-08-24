# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

def plot_GDP(filename):
    # Load data from CSV file
    data = pd.read_csv(filename)

    # Create line plot
    plt.figure(figsize=(8, 6))
    plt.plot(data['China'], label='China')
    plt.plot(data['USA'], label='USA')
    plt.plot(data['Russia'], label='Russia')

    # Set labels and title
    plt.xlabel('Index')
    plt.ylabel('GDP')
    plt.title('Comparative GDP Trends')

    # Add legend
    plt.legend()

    # Set grid and axis limits
    plt.grid(True)
    plt.xlim(0, len(data) - 1)
    plt.ylim(0, max(data.max()))

    # Save the plot
    plt.savefig('GDP_plot.png', dpi=300, bbox_inches='tight')

    # Show the plot
    plt.show()