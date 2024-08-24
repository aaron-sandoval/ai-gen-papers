# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_GDP_growth(filename):
    # Load the data from the CSV file
    data = pd.read_csv(filename)
    
    # Set the style to seaborn-v0_8 for an academic look
    plt.style.use('seaborn-v0_8')
    
    # Create a new figure with 5 inches width and appropriate height
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # Plot the data for each country
    ax.plot(data['Year'], data['China'], label='China', linewidth=1.5)
    ax.plot(data['Year'], data['USA'], label='USA', linewidth=1.5)
    ax.plot(data['Year'], data['Russia'], label='Russia', linewidth=1.5)
    
    # Set the title and labels
    ax.set_title('GDP Growth (1980-2020)', fontsize=10, fontweight='bold')
    ax.set_xlabel('Year', fontsize=8)
    ax.set_ylabel('GDP (Billion USD)', fontsize=8)
    
    # Customize the tick labels
    ax.set_xticks(range(1980, 2021, 10))
    ax.set_xticklabels(range(1980, 2021, 10), rotation=45, ha='right')
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Add a legend
    ax.legend(fontsize=8, loc='upper left')
    
    # Add a grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout to prevent cutoff
    plt.tight_layout()
    
    # Save the plot as a PNG file
    output_filename = filename.replace('.csv', '.png')
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    
    # Close the plot to free up memory
    plt.close()

# Note: This function assumes that the CSV file has the correct format
# with columns: Year, China, USA, Russia