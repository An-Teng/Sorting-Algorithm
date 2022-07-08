def insertionsort(records):
    n = len(records)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = records[i]["CostperPax"]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value < records[pos - 1]["CostperPax"]:
            # Shift the items to the right during the search
            tmp=records[pos]
            records[pos]= records[pos-1]
            pos -= 1
            # Put the saved value into the open slot.
            records[pos] = tmp
    return records
