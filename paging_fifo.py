from collections import deque

# Constants
FRAME_SIZE = 4  # in KB
TOTAL_MEMORY = 64  # in KB
NUM_FRAMES = TOTAL_MEMORY // FRAME_SIZE  # 16 frames

def simulate_paging_fifo(page_references):
    memory = deque()  # queue to represent frames
    page_faults = 0
    memory_set = set()  # fast lookup for page presence

    print("\nSimulating FIFO Paging:")
    print("-" * 30)
    
    for page in page_references:
        if page not in memory_set:
            page_faults += 1
            print(f"Page {page} -> FAULT", end="  ")

            if len(memory) >= NUM_FRAMES:
                removed = memory.popleft()
                memory_set.remove(removed)
                print(f"(Evicted Page {removed})", end="  ")
            
            memory.append(page)
            memory_set.add(page)
        else:
            print(f"Page {page} -> HIT", end="  ")

        print(f"Memory: {list(memory)}")
    
    print("\nTotal Page Faults:", page_faults)
    print("Final Memory State:", list(memory))
    return page_faults

# Sample test case
if __name__ == "__main__":
    page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    simulate_paging_fifo(page_refs)