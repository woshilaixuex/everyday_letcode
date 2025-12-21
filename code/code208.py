class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    def insert(self, word: str) -> None:
        endNode = self
        for c in word:
            index = ord(c) - ord("a")
            if endNode.children[index] is None:
                endNode.children[index] = Trie()
            endNode = endNode.children[index]
        endNode.isEnd = True
    def searchNode(self,pre: str) -> "Trie":
        endNode = self
        for c in pre:
            index = ord(c) - ord("a")
            if endNode.children[index] == None:
                return None
            endNode = endNode.children[index]
        return endNode
    def search(self, word: str) -> bool:
        node = self.searchNode(word)
        return node is not None and node.isEnd
    def startsWith(self, prefix: str) -> bool:
        node = self.searchNode(prefix)
        return node is not None