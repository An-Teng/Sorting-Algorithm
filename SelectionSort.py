def selectionsort(records):
    n = len(records)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if records[j]["Package Name"] < records[smallNdx]["Package Name"]:
                smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest
                # value is not already in its proper position.
        if smallNdx != i:
            tmp = records[i]
            records[i] = records[smallNdx]
            records[smallNdx] = tmp
    return records
