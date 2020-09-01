# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    """
    A simple implementation of a phone book using the direct addressing hash
    method. The method is memory inefficient and in some ways naive during the
    set-up of the array of required size (here 10**7 since max phone num size
    is 7 digits) but all other operations all occur in O(1) time.
    """
    result = []
    contacts = ['' for _ in range(10**7)]
    for cur in queries:
        if cur.type == 'add':
            contacts[cur.number] = cur.name
        elif cur.type == 'del':
            contacts[cur.number] = ""
        else:
            find_name = contacts[cur.number]
            response = 'not found' if not find_name else find_name
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
