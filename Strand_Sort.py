import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def strand_sort(arr):
    sorted_list = []
    frames = []

    # Convert the NumPy array to a list for processing
    arr = arr.tolist()

    while arr:
        # Create a new sorted subsequence
        sub_seq = []
        first = arr.pop(0)
        sub_seq.append(first)

        # Build the subsequence
        for num in arr[:]:  # Iterate over a copy of arr
            if num >= first:
                sub_seq.append(num)
                arr.remove(num)

        # Merge the sorted subsequence into the sorted list
        sorted_list.extend(sub_seq)
        frames.append(sorted_list.copy())  # Capture the current state of the sorted list

    return sorted_list, frames

def strand_sort_visual(arr):
    frames = []
    sorted_arr, frames = strand_sort(arr)

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
    ax.set_title('Strand Sort Visualization', color='white', fontsize=14, pad=20)

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
        status_text.set_text(f"Current Sorted List: {frame}")

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
arr = np.random.randint(1, 100, 20)  # Using a range suitable for Strand Sort

# Run visualization
strand_sort_visual(arr)