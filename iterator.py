class NodeIterator:
    '''
    节点迭代器
    '''
    def __init__(self, root):
        self.root = root
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.root.children):
            raise StopIteration
        self.idx += 1
        return self.root.children[self.idx-1]