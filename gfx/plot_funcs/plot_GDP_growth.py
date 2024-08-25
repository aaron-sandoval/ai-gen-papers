# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GDP_growth(filename):
    # Set the plot style
    plt.style.use('seaborn-v0_8')
    
    # Load the data from the CSV file
    data = pd.read_csv(filename)
    
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(5, 3.5))  # 5 inches wide, adjust height for aspect ratio
    
    # Plot the data for each country
    ax.plot(data['Year'], data['China'], label='China')
    ax.plot(data['Year'], data['USA'], label='USA')
    ax.plot(data['Year'], data['Russia'], label='Russia')
    
    # Set the title and labels
    ax.set_title('GDP Growth Comparison', fontsize=12)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('GDP (USD Billions)', fontsize=10)
    
    # Customize the tick labels
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Add legend
    ax.legend(fontsize=8, loc='upper left')
    
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Save the plot as a PNG file
    plt.savefig(filename.replace('.csv', '.png'), dpi=300, bbox_inches='tight')
    
    # Close the plot to free up memory
    plt.close()

# Example usage:
# plot_GDP_growth('gdp_data.csv')