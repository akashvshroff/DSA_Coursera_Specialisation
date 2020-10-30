# python3
import sys


def BWT(text):
    """
    Return the Burrow-Wheeler Transform a given string.
    This is done by creating a list of all the cyclic rotations of
    the string, sorting them and then fetching all the last characters.
    """
    rev = []
    for i in range(len(text)):
        if not rev:
            rev.append(text[-1] + text[:-1])
        else:
            rev.append(rev[-1][-1] + rev[-1][:-1])
    return ''.join(rs[-1] for rs in sorted(rev))


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
