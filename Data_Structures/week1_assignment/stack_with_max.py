# python3
import sys


class StackWithMax():
    def __init__(self):
        """
        Stack implementation which uses an auxilliary stack that maintains the
        maximum value so far.
        """
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.max_stack:
            self.max_stack.append(a)
        else:
            m_s_f = self.max_stack[-1]  # max so far
            if a > m_s_f:
                self.max_stack.append(a)
            else:
                self.max_stack.append(m_s_f)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
