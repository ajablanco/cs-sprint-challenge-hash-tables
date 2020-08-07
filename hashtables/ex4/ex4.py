def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hash_tbl = {}
    result = []


    for num in a:
        abs_val = abs(num)
        if abs_val in hash_tbl:
            hash_tbl[abs_val] += 1
            result.append(abs_val)
        else:
            hash_tbl[abs_val] = 1

    return result

print(has_negatives([1, -1, 2, -2, 3, 4, 5, -5]))


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
