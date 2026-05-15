def simulate_segmentation(total_memory_kb, segment_sizes):
    memory_used = 0
    memory_layout = []
    external_frag = 0

    print("\n--- Segmentation Simulation ---")
    print(f"Total Available Memory: {total_memory_kb} KB")

    for segment_name, size_kb in segment_sizes.items():
        if memory_used + size_kb <= total_memory_kb:
            memory_layout.append((segment_name, size_kb))
            memory_used += size_kb
            print(f"Segment '{segment_name}' of {size_kb} KB -> ALLOCATED")
        else:
            print(f"Segment '{segment_name}' of {size_kb} KB -> NOT ENOUGH MEMORY")

    external_frag = total_memory_kb - memory_used
    print("\n--- Allocation Result ---")
    for seg in memory_layout:
        print(f"{seg[0]}: {seg[1]} KB")
    
    print(f"\nTotal Used: {memory_used} KB")
    print(f"External Fragmentation: {external_frag} KB")

if __name__ == "__main__":
    total_memory = 64  # KB (as per your CCP constraints)
    
    # Define segment sizes for a process
    segments = {
        "Code": 20,
        "Data": 30,
        "Stack": 16
    }

    simulate_segmentation(total_memory, segments)