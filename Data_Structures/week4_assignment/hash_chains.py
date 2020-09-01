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
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        """
        String hashing using polynomial hashing.
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, hash, s):
        """
        Add a string to the hash-table if it isn't in it already.
        """
        if s not in self.buckets[hash]:
            self.buckets[hash].insert(0, s)

    def check(self, id):
        """
        Print all elements in a particular bucket.
        """
        print(' '.join(self.buckets[id]))

    def find(self, hash, s):
        """
        Return yes if a string is in the hash-table, no if not.
        """
        for elem in self.buckets[hash]:
            if elem == s:
                print('yes')
                return
        print('no')

    def _del(self, hash, s):
        """
        Remove a particular string from the hash-table.
        """
        try:
            self.buckets[hash].remove(s)
        except ValueError:
            pass

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            self.check(query.ind)
        else:
            hash = self._hash_func(query.s)
            if query.type == 'add':
                self.add(hash, query.s)
            elif query.type == 'find':
                self.find(hash, query.s)
            else:
                self._del(hash, query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
