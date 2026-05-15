import math

def simulate_paged_segmentation(total_memory_kb, frame_size_kb, segments):
    total_frames = total_memory_kb // frame_size_kb
    used_frames = 0
    frame_map = []
    page_tables = {}

    print("\n--- Paged Segmentation Simulation ---")
    print(f"Total Memory: {total_memory_kb} KB, Frame Size: {frame_size_kb} KB")
    print(f"Total Frames: {total_frames}\n")

    for segment_name, segment_size in segments.items():
        num_pages = math.ceil(segment_size / frame_size_kb)
        print(f"Segment '{segment_name}' → {segment_size} KB → {num_pages} page(s)")

        if used_frames + num_pages > total_frames:
            print(f"  ❌ Not enough memory to allocate pages for '{segment_name}'\n")
            continue

        frame_indices = list(range(used_frames, used_frames + num_pages))
        page_tables[segment_name] = frame_indices
        used_frames += num_pages
        frame_map.extend([(segment_name, i) for i in range(num_pages)])
        print(f"  ✅ Allocated Frames: {frame_indices}\n")

    print("--- Page Tables ---")
    for seg, frames in page_tables.items():
        print(f"{seg}: Page → Frame Map")
        for i, f in enumerate(frames):
            print(f"  Page {i} → Frame {f}")
        print()

    print(f"Total Frames Used: {used_frames}/{total_frames}")
    print(f"Free Frames: {total_frames - used_frames}")

if __name__ == "__main__":
    total_memory_kb = 64      # As per your CCP
    frame_size_kb = 4         # Fixed page/frame size
    segments = {
        "Code": 20,  # KB
        "Data": 18,
        "Stack": 10
    }

    simulate_paged_segmentation(total_memory_kb, frame_size_kb, segments)