# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_Heights(filename):
    # Set the style
    plt.style.use('seaborn-v0_8')
    
    # Read the CSV file
    data = pd.read_csv(filename)
    
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # Plot the histogram
    ax.hist([data[data['Gender'] == 'Female']['Height'], 
             data[data['Gender'] == 'Male']['Height']], 
            bins=range(54, 66, 1), 
            stacked=True, 
            color=['pink', 'lightblue'], 
            label=['Female', 'Male'])
    
    # Set the title and labels
    ax.set_title('Height Distribution of 12-Year-Old Children', fontsize=10)
    ax.set_xlabel('Height (inches)', fontsize=9)
    ax.set_ylabel('Frequency', fontsize=9)
    
    # Set the x-axis ticks
    ax.set_xticks(range(55, 65, 1))
    
    # Adjust tick label font size
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Add legend
    ax.legend(fontsize=8)
    
    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(filename.replace('.csv', '.png'), dpi=300)
    
    # Close the figure to free up memory
    plt.close(fig)