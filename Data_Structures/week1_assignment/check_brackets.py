# python3


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    """
    Check if all parentheses are balanced, if not return the index position
    (1-based) where the error lies with priority given to closing brackets and
    then opening ones.
    """
    br_stack = []
    id_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            br_stack.append(next)
            id_stack.append(i+1)
        if next in ")]}":
            # Process closing bracket, write your code here
            if br_stack and are_matching(br_stack[-1], next):
                br_stack.pop()
                id_stack.pop()
            else:
                return i + 1
    if br_stack:
        return id_stack[0]
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
