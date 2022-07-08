def mergeSort(records):
    if len(records) > 1:

         # Finding the mid of the array
        mid = len(records)//2

        # Dividing the array elements
        L = records[:mid]

        # into 2 halves
        R = records[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i]["NoPax"] < R[j]["NoPax"]:
                records[k] = L[i]
                i += 1
            else:
                records[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            records[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            records[k] = R[j]
            j += 1
            k += 1
    return records

