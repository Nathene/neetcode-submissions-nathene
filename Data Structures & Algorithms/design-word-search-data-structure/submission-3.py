class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        return self.recursive_search(curr, word)
    
    def recursive_search(self, node: Node, word: str) -> bool:
        if not node:
            return False
        if word == "":
            return node.is_word 
        
        for i, c in enumerate(word):
            if c == ".":
                for child in node.children.values():
                    if self.recursive_search(child, word[i+1:]): return True

                return False
            
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.is_word
        
