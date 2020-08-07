# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_tbl = {}
    result = []

    for file_ in files:
        file_text = file_.split("/")[-1]

        if file_text in hash_tbl:
            hash_tbl[file_text].append(file_)
        else:
            hash_tbl[file_text] = [file_]

    for query in queries:
        if query in hash_tbl:
            for path in hash_tbl[query]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
