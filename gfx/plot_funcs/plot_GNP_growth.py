# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GNP_growth(filename):
    # Set the style
    plt.style.use('seaborn-v0_8')
    
    # Load the data
    df = pd.read_csv(filename)
    
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(5, 3.5))  # 5 inches wide, adjust height for better aspect ratio
    
    # Plot the data
    ax.plot(df['Year'], df['China'], label='China')
    ax.plot(df['Year'], df['USA'], label='USA')
    ax.plot(df['Year'], df['Russia'], label='Russia')
    
    # Set the title and labels
    ax.set_title('GDP Growth 1980-2020', fontsize=12)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('GDP (Billion USD)', fontsize=10)
    
    # Customize the tick labels
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Add legend
    ax.legend(fontsize=8, loc='upper left')
    
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(filename.replace('.csv', '.png'), dpi=300, bbox_inches='tight')
    
    # Close the plot to free up memory
    plt.close()

# Example usage:
# plot_GNP_growth('gdp_data.csv')