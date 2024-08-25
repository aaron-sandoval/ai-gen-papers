from gfx.plot_funcs.import_common import *

def plot_IMG_2(filename):
    # Load data from CSV file
    data = pd.read_csv(filename)

    # Create figure and axes
    fig, ax1 = plt.subplots(figsize=(6, 4))

    # Plot MAE on left y-axis
    ax1.plot(data['Control Number'], data['MAE'], color='blue', label='MAE')
    ax1.set_xlabel('Control Number')
    ax1.set_ylabel('MAE', color='blue')
    ax1.tick_params('y', colors='blue')

    # Create right y-axis for Coverage@10
    ax2 = ax1.twinx()
    ax2.plot(data['Control Number'], data['Coverage@10'], color='red', label='Coverage@10')
    ax2.set_ylabel('Coverage@10', color='red')
    ax2.tick_params('y', colors='red')

    # Add title, legend, and axis labels
    plt.title('DLCRec Performance on Steam Dataset')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)
    ax1.set_xlabel('Control Number', fontsize=10)
    ax1.set_ylabel('MAE', fontsize=10)
    ax2.set_ylabel('Coverage@10', fontsize=10)

    # Save plot as PNG
    plt.savefig(f"{filename.split('.')[0]}.png", dpi=300)