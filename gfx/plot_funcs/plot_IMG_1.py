from gfx.plot_funcs.import_common import *

def plot_IMG_1(filename):
    # Load data from file
    data = pd.read_csv(filename)

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 4))

    # Plot data points
    ax.scatter(data['Diversity'][0:9], data['Accuracy'][0:9], color='r', label='DLCRec')
    ax.scatter(data['Diversity'][9:18], data['Accuracy'][9:18], color='g', label='Baseline 1')
    ax.scatter(data['Diversity'][18:27], data['Accuracy'][18:27], color='b', label='Baseline 2')
    ax.scatter(data['Diversity'][27:], data['Accuracy'][27:], color='y', label='Baseline 3')

    # Add trend lines
    ax.plot(data['Diversity'][0:9], data['Accuracy'][0:9], 'r-', label='DLCRec Trend')
    ax.plot(data['Diversity'][9:18], data['Accuracy'][9:18], 'g-', label='Baseline 1 Trend')
    ax.plot(data['Diversity'][18:27], data['Accuracy'][18:27], 'b-', label='Baseline 2 Trend')
    ax.plot(data['Diversity'][27:], data['Accuracy'][27:], 'y-', label='Baseline 3 Trend')

    # Add labels and title
    ax.set_xlabel('Diversity Score')
    ax.set_ylabel('Accuracy Score')
    ax.set_title('Trade-off between Diversity and Accuracy')
    ax.legend(fontsize=8)

    # Save plot
    plt.savefig(f"{filename.split('.')[0]}.png", dpi=300)