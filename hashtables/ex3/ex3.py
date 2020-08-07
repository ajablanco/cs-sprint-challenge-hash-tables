def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_tbl = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in hash_tbl:
                hash_tbl[num] = 1
            else:
                hash_tbl[num] += 1

    for i in hash_tbl:
        if hash_tbl[i] == len(arrays):
            result.append(i)


    return result


print(intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ]))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
