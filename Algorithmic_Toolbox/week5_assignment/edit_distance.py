# Uses python3


def edit_distance(s, t):
    """
    Compute the edit distance or levenshtein distance for 2 strings.
    """
    if s == t:
        return 0

    if not s:
        return len(t)
    elif not t:
        return len(s)
    rows = len(s) + 1
    cols = len(t) + 1

    s = ' '+s
    t = ' '+t

    D = [[None for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        D[row][0] = row
    for col in range(cols):
        D[0][col] = col

    for row in range(1, rows):
        for col in range(1, cols):
            insertion = D[row-1][col]+1
            deletion = D[row][col-1]+1
            match = D[row-1][col-1]
            mismatch = match + 1
            if s[row] == t[col]:
                D[row][col] = min(insertion, deletion, match)
            else:
                D[row][col] = min(insertion, deletion, mismatch)
    return D[rows-1][cols-1]


if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    print(edit_distance('bread', 'really'))
