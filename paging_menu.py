from collections import deque

def simulate_fifo(page_refs, num_frames):
    memory = deque()
    memory_set = set()
    page_faults = 0

    print("\n--- FIFO Page Replacement ---")
    for page in page_refs:
        if page not in memory_set:
            page_faults += 1
            if len(memory) == num_frames:
                removed = memory.popleft()
                memory_set.remove(removed)
                print(f"Page {page} -> FAULT (Evicted Page {removed})")
            else:
                print(f"Page {page} -> FAULT")
            memory.append(page)
            memory_set.add(page)
        else:
            print(f"Page {page} -> HIT")
        print(f"Memory: {list(memory)}")

    print(f"Total Page Faults: {page_faults}")
    return page_faults

def simulate_lru(page_refs, num_frames):
    memory = []
    last_used = {}
    page_faults = 0
    time = 0

    print("\n--- LRU Page Replacement ---")
    for page in page_refs:
        time += 1
        if page in memory:
            print(f"Page {page} -> HIT")
        else:
            page_faults += 1
            if len(memory) < num_frames:
                print(f"Page {page} -> FAULT")
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: last_used[p])
                memory.remove(lru_page)
                print(f"Page {page} -> FAULT (Evicted Page {lru_page})")
                memory.append(page)
        last_used[page] = time
        print(f"Memory: {memory}")

    print(f"Total Page Faults: {page_faults}")
    return page_faults

def simulate_optimal(page_refs, num_frames):
    memory = []
    page_faults = 0

    print("\n--- Optimal Page Replacement ---")
    for i in range(len(page_refs)):
        page = page_refs[i]
        if page in memory:
            print(f"Page {page} -> HIT")
        else:
            page_faults += 1
            if len(memory) < num_frames:
                memory.append(page)
                print(f"Page {page} -> FAULT")
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
                evicted_page = memory[evict_index]
                memory[evict_index] = page
                print(f"Page {page} -> FAULT (Evicted Page {evicted_page})")
        print(f"Memory: {memory}")

    print(f"Total Page Faults: {page_faults}")
    return page_faults

def main():
    page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    num_frames = 4

    print("=== Memory Management Simulation ===")
    print("Page References:", page_refs)
    print("Number of Frames:", num_frames)
    print("\nChoose a page replacement algorithm:")
    print("1. FIFO")
    print("2. LRU")
    print("3. Optimal")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        simulate_fifo(page_refs, num_frames)
    elif choice == "2":
        simulate_lru(page_refs, num_frames)
    elif choice == "3":
        simulate_optimal(page_refs, num_frames)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()