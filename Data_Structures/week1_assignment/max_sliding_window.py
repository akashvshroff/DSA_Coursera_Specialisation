# python3
class Queue:
    def __init__(self):
        """
        Implements a queue with 2 stacks.
        """
        self.s1 = []
        self.s2 = []
        self.max_stack = []

    def enqueue(self, val):
        self.s1.append(val)

    def swap_stacks(self):
        """
        Puts all the items of stack 1 into stack 2 allowing you to thereby make
        a queue.
        """
        if not self.s2:
            while self.s1:
                item = self.s1.pop()
                self.s2.append(item)
                if self.max_stack:
                    m_s_f = self.max_stack[-1]
                    if item > m_s_f:
                        self.max_stack.append(item)
                    else:
                        self.max_stack.append(m_s_f)
                else:
                    self.max_stack.append(item)

    def dequeue(self):
        self.swap_stacks()
        self.s2.pop()
        self.max_stack.pop()

    def print_max(self):
        self.swap_stacks()
        assert(self.max_stack)
        print(self.max_stack[-1], end=" ")


def max_sliding_window(n, arr, k):
    """
    Solving the maximum sliding window problem using 2 stacks and a max_stack.
    """
    queue = Queue()
    for num in arr[:k]:
        queue.enqueue(num)
    queue.print_max()
    num = k
    for window in range(n-k):
        queue.dequeue()
        queue.enqueue(arr[num])
        queue.print_max()
        num += 1


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    max_sliding_window(n, input_sequence, window_size)
