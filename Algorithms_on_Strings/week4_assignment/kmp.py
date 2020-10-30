# python3

def computer_prefixes(S):
    """
    Preprocesses the string S and returns an array that is
    the prefix function of the string. The prefix function at
    a position returns the longest border of the prefix of the
    song so far.
    """
    n = len(S)
    s = [None] * n
    s[0] = 0
    border = 0
    for i in range(1, n):
        while border and S[i] != S[border]:
            border = s[border - 1]
        if S[i] == S[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    S = pattern + '$' + text
    pre = computer_prefixes(S)
    p = len(pattern)
    for i in range(p + 1, len(S)):
        if pre[i] == p:
            result.append(i-2*p)
    return result


if __name__ == '__main__':
    pattern = input()
    text = input()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
