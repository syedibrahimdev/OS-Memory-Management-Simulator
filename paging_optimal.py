def simulate_paging_optimal(page_references, num_frames):
    memory = []
    page_faults = 0

    print("\nSimulating Optimal Paging:")
    print("-" * 30)

    for i in range(len(page_references)):
        page = page_references[i]

        if page in memory:
            print(f"Page {page} -> HIT", end="  ")
        else:
            page_faults += 1
            print(f"Page {page} -> FAULT", end="  ")

            if len(memory) < num_frames:
                memory.append(page)
            else:
                # Find the page in memory that won't be used for the longest time
                future_refs = page_references[i+1:]
                indices = []
                for m in memory:
                    if m in future_refs:
                        idx = future_refs.index(m)
                    else:
                        idx = float('inf')  # not used again
                    indices.append(idx)

                # Evict the page with the farthest future use
                evict_index = indices.index(max(indices))
                evicted_page = memory[evict_index]
                memory[evict_index] = page
                print(f"(Evicted Page {evicted_page})", end="  ")

        print(f"Memory: {memory}")

    print("\nTotal Page Faults:", page_faults)
    print("Final Memory State:", memory)
    return page_faults

if __name__ == "__main__":
    page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    simulate_paging_optimal(page_refs, num_frames=4)