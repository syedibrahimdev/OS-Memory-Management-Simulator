import math
import matplotlib.pyplot as plt
from collections import deque

# FIFO Page Replacement Algorithm
def simulate_fifo(page_refs, num_frames):
    memory = deque()
    memory_set = set()
    page_faults = 0

    for page in page_refs:
        if page not in memory_set:
            page_faults += 1
            if len(memory) == num_frames:
                removed = memory.popleft()
                memory_set.remove(removed)
            memory.append(page)
            memory_set.add(page)

    return page_faults

# LRU Page Replacement Algorithm
def simulate_lru(page_refs, num_frames):
    memory = []
    last_used = {}
    page_faults = 0
    time = 0

    for page in page_refs:
        time += 1
        if page in memory:
            pass
        else:
            page_faults += 1
            if len(memory) < num_frames:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: last_used[p])
                memory.remove(lru_page)
                memory.append(page)
        last_used[page] = time

    return page_faults

# Optimal Page Replacement Algorithm
def simulate_optimal(page_refs, num_frames):
    memory = []
    page_faults = 0

    for i in range(len(page_refs)):
        page = page_refs[i]
        if page in memory:
            continue

        page_faults += 1
        if len(memory) < num_frames:
            memory.append(page)
        else:
            future_refs = page_refs[i+1:]
            indices = []
            for m in memory:
                if m in future_refs:
                    idx = future_refs.index(m)
                else:
                    idx = float('inf')
                indices.append(idx)
            evict_index = indices.index(max(indices))
            memory[evict_index] = page

    return page_faults

# Segmentation Simulation
def simulate_segmentation(total_memory_kb, segment_sizes):
    memory_used = 0
    memory_layout = []
    external_frag = 0

    for segment_name, size_kb in segment_sizes.items():
        if memory_used + size_kb <= total_memory_kb:
            memory_layout.append((segment_name, size_kb))
            memory_used += size_kb
        else:
            continue

    external_frag = total_memory_kb - memory_used
    return memory_layout, external_frag

# Paged Segmentation Simulation
def simulate_paged_segmentation(total_memory_kb, frame_size_kb, segments):
    total_frames = total_memory_kb // frame_size_kb
    used_frames = 0
    page_tables = {}

    for segment_name, segment_size in segments.items():
        num_pages = math.ceil(segment_size / frame_size_kb)
        if used_frames + num_pages > total_frames:
            continue
        frame_indices = list(range(used_frames, used_frames + num_pages))
        page_tables[segment_name] = frame_indices
        used_frames += num_pages

    free_frames = total_frames - used_frames
    return page_tables, used_frames, free_frames

# Bar Graph for Page Faults
def plot_page_faults(faults):
    algorithms = list(faults.keys())
    values = list(faults.values())

    plt.figure(figsize=(8, 6))
    bars = plt.bar(algorithms, values, color=['red', 'orange', 'green'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.2, yval, ha='center', va='bottom', fontsize=12)

    plt.title('Page Fault Comparison', fontsize=14)
    plt.xlabel('Algorithm')
    plt.ylabel('Page Faults')
    plt.ylim(0, max(values) + 3)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Main Menu
def main():
    while True:
        print("\n=== Memory Management Simulator ===")
        print("1. Simulate Paging")
        print("2. Simulate Segmentation")
        print("3. Simulate Paged Segmentation")
        print("4. Graph Page Faults")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
            num_frames = 4
            print("\n1. FIFO\n2. LRU\n3. Optimal")
            algo = input("Select algorithm: ")

            if algo == '1':
                faults = simulate_fifo(page_refs, num_frames)
                print(f"FIFO Page Faults: {faults}")
            elif algo == '2':
                faults = simulate_lru(page_refs, num_frames)
                print(f"LRU Page Faults: {faults}")
            elif algo == '3':
                faults = simulate_optimal(page_refs, num_frames)
                print(f"Optimal Page Faults: {faults}")
            else:
                print("Invalid algorithm choice.")

        elif choice == '2':
            total_mem = 64
            segments = {"Code": 20, "Data": 30, "Stack": 16}
            layout, frag = simulate_segmentation(total_mem, segments)
            print("\n--- Segment Allocation ---")
            for seg, size in layout:
                print(f"{seg}: {size} KB")
            print(f"External Fragmentation: {frag} KB")

        elif choice == '3':
            total_mem = 64
            frame_size = 4
            segments = {"Code": 20, "Data": 18, "Stack": 10}
            tables, used, free = simulate_paged_segmentation(total_mem, frame_size, segments)
            print("\n--- Paged Segmentation ---")
            for seg, frames in tables.items():
                print(f"{seg}: Page → Frame")
                for i, f in enumerate(frames):
                    print(f"  Page {i} → Frame {f}")
            print(f"Frames Used: {used}, Free Frames: {free}")

        elif choice == '4':
            page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
            num_frames = 4
            results = {
                "FIFO": simulate_fifo(page_refs, num_frames),
                "LRU": simulate_lru(page_refs, num_frames),
                "Optimal": simulate_optimal(page_refs, num_frames)
            }
            plot_page_faults(results)

        elif choice == '5':
            print("Exiting simulator.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()





