def bubblesort(records):
    n = len(records)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if records[j]['Customer Name'] > records[j + 1]['Customer Name']:
                # Swap the j and j+1 items
                tmp = records[j]
                records[j] = records[j + 1]
                records[j + 1] = tmp
    return records
