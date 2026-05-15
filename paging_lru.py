def simulate_paging_lru(page_references, num_frames):
    memory = []
    last_used = {}
    page_faults = 0
    time = 0

    print("\nSimulating LRU Paging:")
    print("-" * 30)

    for page in page_references:
        time += 1
        if page in memory:
            print(f"Page {page} -> HIT", end="  ")
        else:
            page_faults += 1
            print(f"Page {page} -> FAULT", end="  ")

            if len(memory) < num_frames:
                memory.append(page)
            else:
                # Find least recently used page
                lru_page = min(memory, key=lambda p:last_used[p])
                memory.remove(lru_page)
                print(f"(Evicted Page {lru_page})", end="  ")
                memory.append(page)

        last_used[page] = time
        print(f"Memory: {memory}")

    print("\nTotal Page Faults:", page_faults)
    print("Final Memory State:", memory)
    return page_faults

if __name__ == "__main__":
    page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    simulate_paging_lru(page_refs, num_frames=4)