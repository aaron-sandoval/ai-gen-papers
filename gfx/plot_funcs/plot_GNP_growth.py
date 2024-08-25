import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GNP_growth(filename):
    # Load the data from the file
    data = pd.read_csv(filename)

    # Set the style of the plot
    sns.set_style("whitegrid")

    # Create the figure and axis object
    fig, ax = plt.subplots(figsize=(5, 4))

    # Plot the data
    data.plot(x="Year", y=["China", "USA", "Russia"], ax=ax, linewidth=2)

    # Set the title, legend, axis labels, and tick labels
    ax.set_title("GDP Growth by Country", fontsize=12)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("GDP (USD)", fontsize=10)
    ax.tick_params(axis="both", labelsize=8)
    ax.legend(fontsize=8)

    # Save the plot as a PNG file
    plt.savefig(f"{filename.split('.')[0]}.png", dpi=300)