# python3

import sys


def get_hash_value(table, prime, multiplier, start, length):
    """
    Returns the hash_value for any substring of a string using the pre-computed
    hash table.
    """
    y = pow(multiplier, length, prime)
    hash_value = (table[start+length] - y*table[start]) % prime
    return hash_value


def pre_compute_hashes(s, M1, M2, X):
    """
    Pre-compute hash-table for a string with 2 prime numbers and a multiplier.
    Using a rolling hash function, we can get the hash-value for any substring
    in constant time.
    """
    n = len(s)
    h1 = [0 for _ in range(n+1)]
    h2 = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        ch = ord(s[i-1])
        h1[i] = (X*h1[i-1] + ch) % M1
        h2[i] = (X*h2[i-1] + ch) % M2
    return h1, h2


def find_num_matches(p1, p2, t1, t2, m1, m2, x, k, len_p, i):
    """
    Uses binary search to find the number of mismatches. It finds the left-most
    mismatch and then looks at the substring hash after that index position and
    continues until the number of mismatches are more than k or the start pointer
    is more than or equal to end.
    """
    start = 0
    for mismatch in range(k):
        # print(f'start: {start}, id: {id}')
        id = start
        end = len_p-1
        while start <= end:
            mid = start + (end-start)//2
            p_h1, p_h2 = get_hash_value(
                p1, m1, x, id, mid-start), get_hash_value(p2, m2, x, id, mid-start)
            s_h1, s_h2 = get_hash_value(
                t1, m1, x, i+id, mid-start), get_hash_value(t2, m2, x, i+id, mid-start)
            if p_h1 == s_h1 and p_h2 == s_h2:  # move to the right half, no mismatch yet
                start = mid + 1
            else:
                end = mid - 1
        # when loop exits, start - 1 is the index of the mismatch.
        if start == len_p:  # found the last mismatch
            return True
    return False


def solve(k, text, pattern):
    """
    Driver function to return number of occurences of a pattern in a text with
    at most k mismatches. Returns the start index of occurence as well as the
    number of mismatches.
    """
    # print(k, text, pattern)
    base = pow(10, 9)
    M1 = base + 7
    M2 = base + 9
    X = 263
    len_p = len(pattern)
    len_t = len(text)
    pattern1, pattern2 = pre_compute_hashes(pattern, M1, M2, X)
    text1, text2 = pre_compute_hashes(text, M1, M2, X)
    res = []
    p_hash1, p_hash2 = get_hash_value(
        pattern1, M1, X, 0, len_p), get_hash_value(pattern2, M2, X, 0, len_p)
    for i in range(len_t-len_p+1):  # all possible candidates
        subs_hash1 = get_hash_value(text1, M1, X, i, len_p)
        subs_hash2 = get_hash_value(text2, M2, X, i, len_p)
        is_valid = find_num_matches(pattern1, pattern2, text1, text2, M1, M2, X, k, len_p, i)
        if is_valid:
            res.append(i)
    return res


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = solve(int(k), t, p)
        print(len(ans), *ans)
