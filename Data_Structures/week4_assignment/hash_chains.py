# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    """
    Simple hashing using chaining amongst user-defined number of buckets.
    """
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        """
        String hashing using polynomial hashing.
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind][::-1])
        else:
            hash_ind = self._hash_func(query.s)
            if query.type == 'find':
                bucket = self.elems[hash_ind]
                found = False
                for str_ in bucket:
                    if str_ == query.s:
                        found = True
                        break
                self.write_search_result(found)
            elif query.type == 'add':
                self.elems[hash_ind].append(query.s)
            else:
                bucket = self.elems[hash_ind]
                self.elems[hash_ind] = [elem for elem in bucket if elem != query.s]

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
