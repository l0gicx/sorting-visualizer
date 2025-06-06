import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def counting_sort_visual(arr):
    max_val = max(arr)  # Find the maximum value in the array
    count = [0] * (max_val + 1)  # Create a count array

    # Count occurrences of each value
    for num in arr:
        count[num] += 1

    # Prepare the output array
    output = []
    frames = []

    # Build the output array based on the count array
    for i in range(len(count)):
        while count[i] > 0:
            output.append(i)
            count[i] -= 1
            frames.append(output.copy())  # Capture the current state of the output array

    # Set up modern dark theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')
    ax.set_facecolor('#1a1a1a')

    # Create bars with black color and white edges
    bar_rects = ax.bar(range(len(arr)), arr, 
                      color='black', 
                      edgecolor='white',
                      linewidth=1.5,
                      width=0.8)

    # Styling
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    ax.tick_params(axis='both', colors='white', labelsize=10)
    ax.set_title('Counting Sort Visualization', color='white', fontsize=14, pad=20)

    # Remove top/right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')

    # Status text
    status_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, 
                         color='white', fontsize=12)

    # Animation update function
    def update(frame):
        # Update heights
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)

        # Update status text
        status_text.set_text(f"Current Output: {frame}")

        return list(bar_rects) + [status_text]  # Convert bar_rects to a list

    # Create the animation
    anim = animation.FuncAnimation(
        fig, update,
        frames=frames,
        interval=500,  # Adjust for speed of animation
        blit=True,
        repeat=False
    )

    plt.tight_layout()
    plt.show()

# Generate random data
np.random.seed(42)
arr = np.random.randint(0, 10, 20)  # Using a smaller range for counting sort

# Run visualization
counting_sort_visual(arr)