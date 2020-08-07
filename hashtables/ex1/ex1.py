def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_tbl = {}

    for i in range(length):
        current = weights[i]

        # find the complement 
        complement = (limit - current)

        # if complement exists in tbl, return (current idx, complement idx)
        if complement in hash_tbl:
            comp_indx = hash_tbl[complement]

            # return tuple
            return (i, comp_indx)

        else:
            # set value of key = index
            hash_tbl[current] = i


    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
