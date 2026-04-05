class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        root = trie.root
        res = []

        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])

        def search(r: int, c: int, node: Node, path):
            char = board[r][c]

            curr_node = node.children[char]

            if curr_node.is_word:
                res.append(path + char)
                curr_node.is_word = False

            board[r][c] = "#"

            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    nei = board[nr][nc]
                    if nei in curr_node.children:
                        search(nr, nc, curr_node, path + char)
            
            board[r][c] = char

            if not curr_node.children:
                node.children.pop(char)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    search(r, c, root, "")
        
        return res

    

                
                    
class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.is_word = True






        