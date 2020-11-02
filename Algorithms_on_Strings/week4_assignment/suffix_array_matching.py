# python3

def sort_chars(s, chars):
    """
    Sort the characters of the string S in linear time using the
    counting sort method.
    """
    n = len(s)
    order = [None] * n
    count = [0] * n
    chars = [ch for ch in chars if ch in s]
    ch = {c: id for id, c in enumerate(chars)}
    for i in range(n):
        count[ch[s[i]]] += 1
    for j in range(1, len(chars)):
        count[j] += count[j - 1]
    for i in range(n - 1, -1, -1):
        c_id = ch[s[i]]
        count[c_id] -= 1
        order[count[c_id]] = i
    return order


def compute_classes(s, order):
    """
    Compute the equivalence classes for each of the shifted cycles of length L.
    """
    n = len(s)
    class_ = [None] * n
    class_[order[0]] = 0
    for i in range(1, n):
        if s[order[i]] != s[order[i - 1]]:
            class_[order[i]] = class_[order[i - 1]] + 1
        else:
            class_[order[i]] = class_[order[i - 1]]
    return class_


def sort_doubled(s, L, order, class_):
    """
    Using the sorted cyclic shift of L characters, sort the cyclic shift of 2L
    characters.
    """
    n = len(s)
    count = [0] * n
    new_order = [None] * n
    for i in range(n):
        count[class_[i]] += 1
    for j in range(1, n):
        count[j] += count[j - 1]
    for i in range(n - 1, -1, -1):
        start = (order[i] - L + n) % n
        cl = class_[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_class(order, class_, L):
    """
    Update the class equivalence for L characters with the corresponding equivalence
    for 2L characters.
    """
    n = len(order)
    new_class = [None] * n
    new_class[order[0]] = 0
    for i in range(1, n):
        cur = order[i]
        prev = order[i - 1]
        mid = (cur + L) % n
        mid_prev = (prev + L) % n
        if class_[cur] != class_[prev] or class_[mid] != class_[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class


def build_suffix_array(text, chars=['$', 'A', 'C', 'G', 'T']):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = []
    order = sort_chars(text, chars)
    class_ = compute_classes(text, order)
    L = 1
    while L < len(text):
        order = sort_doubled(text, L, order, class_)
        class_ = update_class(order, class_, L)
        L = 2*L
    return order[1:]


def match_with_suffix(t, p, sa):
    """
    Use the suffix array to return the starting index of the pattern
    in text if the pattern appears.
    """
    min = 0
    max = len(t)
    while min < max:
        mid = (min + max) // 2
        suffix = sa[mid]
        i = 0
        while i < len(p) and suffix + i < len(t):
            if p[i] > t[suffix + i]:
                min = mid + 1
                break
            elif p[i] < t[suffix + i]:
                max = mid
                break
            i += 1
            if i == len(p):
                max = mid
            elif suffix + i == len(t):
                min = mid + 1
    start = min
    max = len(t)
    while min < max:
        mid = (min + max) // 2
        suffix = sa[mid]
        i = 0
        while i < len(p) and suffix + i < len(t):
            if p[i] < t[suffix + i]:
                max = mid
                break
            i += 1
            if i == len(p) and i <= len(t) - suffix:
                min = mid + 1
    end = max - 1
    return start, end


def find_occurrences(text, patterns):
    """
    Driver function to generate the suffix array and then use it
    to call upon the pattern matching for each function and then
    print the starting position of all matches.
    """
    suffix_arr = build_suffix_array(text+'$')
    res = [0]*len(text)
    for pattern in patterns:
        s, e = match_with_suffix(text, pattern, suffix_arr)
        if s <= e:
            for i in range(s, e + 1):
                pos = suffix_arr[i]
                if res[pos] == 0:  # not printed yet
                    print(pos, end=' ')
                res[pos] += 1


if __name__ == '__main__':
    text = input()
    n = int(input())
    patterns = input().split()
    find_occurrences(text, patterns)
